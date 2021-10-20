import numpy as np
import cv2
import easyocr
from matplotlib import pyplot as plt

cv2.namedWindow("goster", cv2.WINDOW_NORMAL)
IMAGE_PATH = "fontt.png"

reader = easyocr.Reader(["en"],gpu=False)
result = reader.readtext(IMAGE_PATH)

top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX


img = cv2.imread(IMAGE_PATH)
img = cv2.rectangle(img, top_left, bottom_right, (0,255,0), 5)
img = cv2.putText(img, text, top_left ,font, .5,(0,255,0),2, cv2.LINE_AA)
cv2.imshow("goster", img)

cv2.waitKey(5)
