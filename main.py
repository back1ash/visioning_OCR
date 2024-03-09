import numpy as np
from PIL import Image
import pytesseract

class Tesseract():
  def __init__(self):
    pass

  def setPath(self, path):
    self.path = path
    pytesseract.pytesseract.tesseract_cmd = r"{}".format(path)
    
  def translate(self, path):
    filename = path
    img = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img)
    return text