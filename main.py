import numpy as np
from pytesseract import Output
from PIL import Image
import pytesseract
import cv2

# Tesseract 사용전에 exe 파일 경로를 지정해줘야 한다. 사용자의 경로에 맞춰서 지정하면 된다.
pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract\tesseract.exe"

# GUI를 구현하고, GUI에서 User file을 받아 OCR 처리
filename = r'visioning_OCR\sample\sample2.png'
img = np.array(Image.open(filename))
text = pytesseract.image_to_string(img)
print(text)
