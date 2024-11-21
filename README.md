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
