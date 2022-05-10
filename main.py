import os
# ! Above is for directory navigation
# ! Open-CV import
import cv2
# ! For directory selection GUI
import tkinter as tk
from tkinter import filedialog
# ! imports Tesseract OCR(Optical Character Recognition) package
import pytesseract

# ! tells python where the exe for the OCR is
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# ! Root window of GUI
root = tk.Tk()
# ! hides root window so only the dialog is show
root.withdraw()

# ! sets directory to variable path
path = filedialog.askdirectory()

# ! Create list of files in a directory
files = os.listdir(path)

# ! list containing all image formats supported by Open-CV
imgExts = [".bmp", ".dib", ".jpeg", ".jpg", ".jpe", ".jp2", ".png", ".webp", ".pbm", ".pgm",
           ".ppm", ".pxm", ".pnm", ".pfm", ".sr", ".ras", ".tiff", ".tif", ".exr", ".hdr", ".pic"]

# ! creates empty array to hold image information and eventually string of text found in image if any
imgList = []

# ! Iterates through files to return lists of images
for file in files:
    for imgExt in imgExts:
        if imgExt in file:
            imgPath = path + "/" + file
            temp = [file, imgPath, ""]
            imgList.append(temp)

for img in imgList:
    print(img[1])
    pic = cv2.imread(img[1])
    text = pytesseract.image_to_string(pic)
    img[2] = text

print(imgList)
