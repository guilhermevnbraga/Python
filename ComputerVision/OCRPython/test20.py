import cv2
import pytesseract
import numpy as np
from imutils.object_detection import non_max_suppression


def dadosGeometricos(geometry, y):
  xData0 = geometry[0, 0, y]
  xData1 = geometry[0, 1, y]
  xData2 = geometry[0, 2, y]
  xData3 = geometry[0, 3, y]
  dataAngulos = geometry[0, 4, y]
  return dataAngulos, xData0, xData1, xData2, xData3


def calculosGeometria(dataAngulos, xData0, xData1, xData2, xData3):
  (offsetX, offsetY) = (x * 4.0, y * 4.0)
  angulo = dataAngulos[x]
  cos = np.cos(angulo)
  sin = np.sin(angulo)
  h = xData0[x] + xData2[x]
  w = xData1[x] + xData3[x]

  fimX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
  fimY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
  
  inicioX = int(fimX - w)
  inicioY = int(fimY - h)

  return inicioX, inicioY, fimX, fimY


detector = r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Modelos\frozen_east_text_detection.pb'
largura, altura = 320, 320
imagem = r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Imagens\caneca.jpg'
confiancaMin = 0.9

img = cv2.imread(imagem)

original = img.copy()

H, W = img.shape[0], img.shape[1]
proporcaoH, proporcaoW = H / float(altura), W / float(largura)
img = cv2.resize(img, (largura, altura))
H, W = img.shape[0], img.shape[1]
cv2.imshow('imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

nomesCamadas = ['feature_fusion/Conv_7/Sigmoid', 'feature_fusion/concat_3']
redeNeural = cv2.dnn.readNet(detector)

blob = cv2.dnn.blobFromImage(img, 1.0, (W, H), swapRB = True, crop = False)
redeNeural.setInput(blob)
scores, geometry = redeNeural.forward(nomesCamadas)
linhas, colunas = scores.shape[2:4]

caixas = []
confiancas = []
for y in range(0, linhas):
  dataScores = scores[0, 0, y]

  dataAngulos, xData0, xData1, xData2, xData3 = dadosGeometricos(geometry, y)

  for x in range(0, colunas):
    if dataScores[x] < confiancaMin:
      continue
    
    inicioX, inicioY, fimX, fimY = calculosGeometria(dataAngulos, xData0, xData1, xData2, xData3)
    confiancas.append(dataScores[x])
    caixas.append((inicioX, inicioY, fimX, fimY))
deteccoes = non_max_suppression(np.array(caixas), probs=confiancas)

copia = original.copy()
margem = 1
for (inicioX, inicioY, fimX, fimY) in deteccoes:
  inicioX = int(inicioX * proporcaoW)
  inicioY = int(inicioY * proporcaoH)
  fimX = int(fimX * proporcaoW)
  fimY = int(fimY * proporcaoH)

  # roi -> region of interest
  roi = copia[inicioY-margem:fimY+margem, inicioX-margem:fimX+margem]

  cv2.rectangle(original, (inicioX-margem, inicioY-margem), (fimX+margem, fimY+margem), (0,255,0), 2)
cv2.imshow('imagem', original)
cv2.waitKey(0)
cv2.destroyAllWindows()

roi = cv2.resize(roi, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow('imagem', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

tessdataDir = r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\tessdata'
configTessdata = f'--tessdata-dir "{tessdataDir}" --psm 7'
text = pytesseract.image_to_string(roi, lang='por', config=configTessdata)
print(text)
