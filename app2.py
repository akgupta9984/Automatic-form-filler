import cv2
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re


def preprocess_image(image_path):
    print("Loading image...")
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return None

    print("Image loaded successfully.")
    

    height, width = image.shape[:2]
    new_width = 1000
    aspect_ratio = width / height
    new_height = int(new_width / aspect_ratio)
    image = cv2.resize(image, (new_width, new_height))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

 
    _, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    
    blurred_image = cv2.GaussianBlur(binary_image, (5, 5), 0)

    processed_image = cv2.medianBlur(blurred_image, 3)

    print("Image preprocessed successfully.")
    return processed_image



def extract_text(processed_image):
    print("Extracting text from image...")
    text = pytesseract.image_to_string(processed_image)
    print(f"Extracted text:\n{text}")
    return text

def extract_fields(text):
    print("Extracting fields using regex...")
    fields = {}

    phone_match = re.search(r'Phone no\.:?\s*(\d{3}[\s/-]?\d{6}|\d{10})', text)
    if phone_match:
        fields['Phone'] = phone_match.group(1)

    email_match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    if email_match:
        fields['Email'] = email_match.group()

    org_match = re.search(r'Delivery Chal\w*\s*for\s*(.*?)(?:\n|$)', text)
    if org_match:
        fields['Organization'] = org_match.group(1).strip()

    print(f"Extracted fields: {fields}")
    return fields


def fill_form(fields):
    print("Filling the form...")
    driver = webdriver.Chrome()

    try:
        
        driver.get("https://forms.gle/mBB9TNjmUdbyGDug7")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "form")))

       
        if 'Phone' in fields:
            try:
                phone_field = driver.find_element(By.XPATH, "//input[@type='tel']") 
                phone_field.send_keys(fields['Phone'])
            except NoSuchElementException:
                print("Phone field not found.")

        if 'Email' in fields:
            try:
                email_field = driver.find_element(By.XPATH, "//textarea[@aria-labelledby='i1 i4']") 
                email_field.send_keys(fields['Email'])
            except NoSuchElementException:
                print("Email field not found.")



        if 'Organization' in fields:
            try:
                org_field = driver.find_element(By.XPATH, "//input[@type='text']")  
                org_field.send_keys(fields['Organization'])
            except NoSuchElementException:
                print("Organization field not found.")

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

image_path = "/Users/ayush/Desktop/minor project/static/uploads/WhatsApp Image 2024-10-03 at 22.13.40.jpeg"

processed_image = preprocess_image(image_path)
if processed_image is not None:
    text = extract_text(processed_image)
    fields = extract_fields(text)
    fill_form(fields)
