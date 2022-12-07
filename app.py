# Import the necessary libraries

import csv

import pytesseract

from PIL import Image

from pytesseract_ocr import PyTesseractOCR

# Open the image and convert it to grayscale

image = Image.open('driving_license.png')

gray = image.convert('L')

# Create a PyTesseractOCR object and set the OCR engine mode to LSTM (long short-term memory)

pytesseract_ocr = PyTesseractOCR()

pytesseract_ocr.set_mode('lstm')

# Run the OCR on the image

text = pytesseract_ocr.image_to_string(gray)

# Write the text to a CSV file

with open('output.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([text])

