from PIL import Image
import matplotlib.pyplot as plt
import pytesseract

img = Image.open('/home/s0la1r3/Documentos/GitHub/Python/ComputerVision/OCRPython/Imagens/livro01.jpg')
plt.imshow(img);
plt.axis('off')
plt.show()
text = pytesseract.image_to_osd(img)
print(text)
