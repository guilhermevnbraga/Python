import cv2

img = cv2.imread(r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Imagens\livro_adaptativa.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adapatMediaGauss = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)
cv2.imshow('imaagem', adapatMediaGauss)
cv2.waitKey(0)
cv2.destroyAllWindows()

adapatMediaGauss = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)
cv2.imshow('imagem', adapatMediaGauss)
cv2.waitKey(0)
cv2.destroyAllWindows()
