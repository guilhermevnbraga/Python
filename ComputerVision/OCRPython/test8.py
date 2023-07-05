import cv2
import pytesseract
import re
from pytesseract import Output

img = cv2.imread(r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Imagens\tabela_teste.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
tessdataDir = r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\tessdata'
configTesseract = f'--tessdata-dir "{tessdataDir}"'
resultado = pytesseract.image_to_data(rgb, config=configTesseract, lang='por', output_type=Output.DICT)
