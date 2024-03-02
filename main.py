import numpy as np
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract\tesseract.exe"
class Tesseract():
  def __init__(self):
    pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract\tesseract.exe"
    pass
    
  def translate(path):
    filename = path
    img = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img)
    return text