import cv2 as cv
import os
import pytesseract
import re
import csv

#describing the path of the folder
folder_path = r'E:\Tata Steel Internship\GatePass'

#listing the files in the req dir
file_list = os.listdir(folder_path)

#to print the req txt (gatepass no.) in a txt file
with open(r"E:\Tata Steel Internship\Output\Employee1.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "GatePass No"])
    #using for loop to execute the code to all the gaepass at the sametime
    for file in file_list:
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
            #connecting the filename with folder for appropriate location
            file_path = os.path.join(folder_path, file)
            #reading the image
            img = cv.imread(file_path)
            #converting it to grayscale
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            #large img helps in better and more precise character detection
            re_gray = cv.resize(gray, None, fx=2.2, fy=2.2, interpolation=cv.INTER_CUBIC)
            #thresholding for better output
            threshold, thresh = cv.threshold(re_gray, 134, 255, cv.THRESH_BINARY)
            #extracting txt from the processed img
            text = pytesseract.image_to_string(thresh, config='--psm 6') 
            #regex for selecting only the gatepass
            gate = re.search(r'GatePass ?No\s*[:\-]?\s*([A-Z0-9]+)', text)
            #labeling the numbers with filename for later identification
            name = re.search(r'Name\s*[:\-]?\s*([A-Z.\s]{2,})', text)
            name1 = name.group(1).strip() if name else "NOT FOUND"
            gate1 = gate.group(1).strip() if gate else "NOT FOUND"
            # if not gate1.startswith("JP") and gate1 != "NOT FOUND":
            #     gate1 = "JP" + gate1[2:]
            # clean_text = gatepass.strip()
            writer.writerow([name1, gate1])