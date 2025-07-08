import cv2 as cv
import pytesseract
import re

img = cv.imread(r'E:\Tata Steel Internship\GatePass\IMG-20250626-WA0019.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
re_gray = cv.resize(gray, None, fx=2.2, fy=2.2, interpolation=cv.INTER_CUBIC)
threshold, thresh = cv.threshold(re_gray, 134, 255, cv.THRESH_BINARY)
text = pytesseract.image_to_string(thresh, config='--psm 6') 
#use --psm6 for best result alternatively use psm3 or 4
gatepass = re.search(r'GatePass ?No\s*[:\-]?\s*([A-Z0-9]+)', text)

if gatepass:
    print("GatePass No:", gatepass.group(1))  # ✅ get just the ID part
else:
    print("GatePass No not found.")
# print(text)