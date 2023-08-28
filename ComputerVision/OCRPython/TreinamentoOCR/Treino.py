import tensorflow
import numpy as np
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow.keras.datasets import mnist

(trainData, trainLabels), (testData, testLabels) = mnist.load_data()

print(trainData.shape, testData.shape)
