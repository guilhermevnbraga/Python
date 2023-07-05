from PIL import Image
import matplotlib.pyplot as plt
import pytesseract

img = Image.open(r'.\Imagens\livro01.jpg')
plt.imshow(img);
text = pytesseract.image_to_osd(img)
print(text)
