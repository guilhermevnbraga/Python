import cv2

img = cv2.imread(r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Imagens\trecho-livro.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

val, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
cv2.imshow('imagem', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
