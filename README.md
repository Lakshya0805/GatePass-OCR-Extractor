# GatePass OCR Extractor

This is a simple Python project that uses **OpenCV**, **Tesseract OCR**, and **Regex** to extract the **GatePass Number** from gatepass images and save the results into a CSV file.

## How it works

- Reads all image files from the `GatePass/` folder
- Converts each image to grayscale, resizes it, and applies thresholding
- Uses Tesseract to extract text from each image
- Applies regex to find and extract the Name and GatePass No.

## Requirements

- Python 3
- OpenCV (`opencv-python`)
- Pytesseract (`pytesseract`)
- Regex (`re`, built-in)

Make sure Tesseract OCR is installed on your system and added to PATH.

## How to run

1. Place gatepass images in the `GatePass/` folder  
2. Run the script:

```bash
python gatepass_ocr.py
