import cv2
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

# Preprocess the image to enhance the text
def preprocess_image(image_path):
    print("Loading image...")
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return None

    print("Image loaded successfully.")
    
    # Resize image if necessary
    height, width = image.shape[:2]
    new_width = 1000
    aspect_ratio = width / height
    new_height = int(new_width / aspect_ratio)
    image = cv2.resize(image, (new_width, new_height))

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Thresholding
    _, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(binary_image, (5, 5), 0)

    processed_image = cv2.medianBlur(blurred_image, 3)

    print("Image preprocessed successfully.")
    return processed_image


# Extract text from image using OCR
def extract_text(processed_image):
    print("Extracting text from image...")
    text = pytesseract.image_to_string(processed_image)
    print(f"Extracted text:\n{text}")
    return text

# Extract email, phone, and other fields from the text
def extract_fields(text):
    print("Extracting fields using regex...")
    fields = {}

    # Extract phone number (10 digits, possibly with spaces or dashes)
    phone_match = re.search(r'Phone no\.:?\s*(\d{3}[\s/-]?\d{6}|\d{10})', text)
    if phone_match:
        fields['Phone'] = phone_match.group(1)

    # Extract email address (improved regex)
    email_match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    if email_match:
        fields['Email'] = email_match.group()

    # Extract organization name
    org_match = re.search(r'Delivery Chal\w*\s*for\s*(.*?)(?:\n|$)', text)
    if org_match:
        fields['Organization'] = org_match.group(1).strip()

    print(f"Extracted fields: {fields}")
    return fields

# Step 4: Automate Form Filling with Selenium
def fill_form(fields):
    print("Filling the form...")
    driver = webdriver.Chrome()

    try:
        # Open the Google Form
        driver.get("https://forms.gle/mBB9TNjmUdbyGDug7")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        # Fill in the fields
        if 'Phone' in fields:
            try:
                phone_field = driver.find_element(By.XPATH, "//input[@type='tel']")  # Adjust selector as needed
                phone_field.send_keys(fields['Phone'])
            except NoSuchElementException:
                print("Phone field not found.")

        if 'Email' in fields:
            try:
                email_field = driver.find_element(By.XPATH, "//textarea[@aria-labelledby='i1 i4']")  # Adjust based on actual attributes
                email_field.send_keys(fields['Email'])
            except NoSuchElementException:
                print("Email field not found.")



        if 'Organization' in fields:
            try:
                org_field = driver.find_element(By.XPATH, "//input[@type='text']")  # Adjust selector as needed
                org_field.send_keys(fields['Organization'])
            except NoSuchElementException:
                print("Organization field not found.")

        # Submit the form
        try:
            submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
            submit_button.click()
            print("Form submitted successfully!")
        except NoSuchElementException:
            print("Submit button not found.")

    except Exception as e:
        print(f"Error interacting with the form: {e}")
    finally:
        driver.quit()

# Main Execution
image_path = "/Users/ayush/Desktop/minor project/static/uploads/WhatsApp Image 2024-10-03 at 22.13.40.jpeg"

# Step-by-step processing
processed_image = preprocess_image(image_path)
if processed_image is not None:
    text = extract_text(processed_image)
    fields = extract_fields(text)
    fill_form(fields)
