# Automatic Form Filler

## Overview

The Automatic Form Filler project is a web application that allows users to upload an image containing text, which is then processed to extract relevant fields (such as phone number, email, and organization name) using Optical Character Recognition (OCR). The extracted data is automatically filled into a Google Form using Selenium for web automation.

## Features

- Upload an image file containing text.
- Extract text from the image using Tesseract OCR.
- Automatically fill out a Google Form with the extracted information.
- Handle common fields like phone number, email address, and organization name.

## Technologies Used

- Flask: A lightweight WSGI web application framework in Python.
- OpenCV: A library for computer vision tasks.
- Tesseract: An OCR engine for text extraction from images.
- Selenium: A web automation tool for filling out forms in a browser.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- pip (Python package installer)
- Google Chrome browser
- ChromeDriver (compatible with your version of Chrome)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/automatic-form-filler.git
   cd automatic-form-filler
   ```

2. **Install the required Python packages:**

   Use pip to install the necessary libraries:

   ```bash
   pip install Flask opencv-python pytesseract selenium
   ```

3. **Install Tesseract OCR:**

   - For macOS: You can install Tesseract using Homebrew:

     ```bash
     brew install tesseract
     ```

   - For Windows: Download the installer from Tesseract at UB Mannheim and add the installation path to your system's PATH variable.

4. **Download ChromeDriver:**

   Download the ChromeDriver that matches your Chrome version from [ChromeDriver downloads](https://sites.google.com/a/chromium.org/chromedriver/).
   Ensure the ChromeDriver executable is in your system's PATH.

## Project Structure

```plaintext
automatic-form-filler/
├── app2.py             # Script for processing the image and filling the form
├── chech2.py           # Flask application for handling file uploads
├── templates/
│   └── index.html      # HTML file for the upload form
└── static/
    └── uploads/        # Directory for storing uploaded files
```

## Usage

1. **Run the Flask Application:**

   Start the Flask server by running the following command:

   ```bash
   python chech2.py
   ```

   The application will start and be accessible at http://127.0.0.1:5000/.

2. **Upload an Image:**

   Open your web browser and navigate to http://127.0.0.1:5000/.
   Use the upload form to select and upload an image containing the text you want to extract.

3. **Processing:**

   After uploading, the application will process the image, extract the text, and fill out the specified Google Form using the extracted data.

## Notes

- Ensure that the Google Form URL in `app2.py` is updated to the correct form you wish to fill out.
- The XPath selectors used in the Selenium part may need to be adjusted based on the actual structure of the Google Form.
- Make sure to have the correct permissions set for the uploaded files directory.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```
