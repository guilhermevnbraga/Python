import cv2

img = cv2.imread(r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Imagens\img-process.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

maior = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow('imagem', maior)
cv2.waitKey(0)
cv2.destroyAllWindows()

menor = cv2.resize(gray, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow('imagem', menor)
cv2.waitKey(0)
cv2.destroyAllWindows()
