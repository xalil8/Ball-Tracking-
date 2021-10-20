"""import cv2
cv2.namedWindow("asdas",cv2.WINDOW_NORMAL)
img = cv2.imread("fontt.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#qret, threshold = cv2.threshold(img, 50, 170, cv2.THRESH_BINARY)
#bitwise = cv2.bitwise_not(threshold)
#threshold = cv2.bitwise_not(img)
cv2.imshow("asdas", img)
cv2.waitKey(0)

ali = {"img1":15,"img2":16,"img3":17,"img4":18,"img5":19}"""

"""for x , y in ali.items():
    print(y)"""

from os import listdir
from os.path import isfile, join
import random

import cv2 as cv
"""x, y = ali
print(y)

h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]
h3, w3 = img3.shape[:2]

print(w1)
# create empty matrix
vis = np.zeros((max(h1, h2, h3), w1 + w2 + w3, 3), np.uint8)
vis.fill(255)
# combine 2 images
vis[:h1, :w1, :3] = img1
vis[:h2, w1:w1 + w2, :3] = img2
vis[:h3, w1 + w2:w1 + w2 + w3, :3] = img3

vis_first =
for m in range(num_of_let):
    vis[:heights[f"h{m}"], :widths[f"w{m}"], 3] = image_list[m]"""


ali = "ASDE.png"

print(ali[:-4])

img =cv2.imread("letters_new/low_g.png")

cv2.imshow("asdasd",cv2.flip(img,-1))
cv2.waitKey(1)

def normal():
    cv2.namedWindow("test", cv.WINDOW_NORMAL)

    img1 = cv.imread("letters/A.png")
    img2 = cv.imread("letters/O.png")
    img3 = cv.imread("letters/low_g.png")
    """h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    vis = np.zeros((max(h1, h2), w1+w2), np.uint8)
    vis[:h1, :w1] = img1
    vis[:h2, w1:w1+w2] = img2
    """
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    h3, w3 = img3.shape[:2]
    print(w1)
    #create empty matrix
    vis = np.zeros((max(h1, h2, h3), w1+w2+w3,3), np.uint8)
    vis.fill(255)
    #combine 2 images
    vis[:h1, :w1,:3] = img1
    vis[:h2, w1:w1+w2,:3] = img2
    vis[:h3, w1+w2:w1+w2+w3,:3] = img3

    cv.imshow("test", vis)
    cv.waitKey(0)

def optimized():
    cv2.namedWindow("test", cv.WINDOW_NORMAL)
    img1 = cv.imread("letters/A.png")
    img2 = cv.imread("letters/M.png")
    img3 = cv.imread("letters/low_g.png")
    """h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    vis = np.zeros((max(h1, h2), w1+w2), np.uint8)
    vis[:h1, :w1] = img1
    vis[:h2, w1:w1+w2] = img2
    """
    x = 50
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    h3, w3 = img3.shape[:2]
    h3 = h3 + x
    print(h1)
    # create empty matrix
    vis = np.zeros((max(h1, h2, h3), w1 + w2 + w3, 3), np.uint8)
    vis.fill(255)
    # combine 2 images
    vis[:h1, :w1, :3] = img1
    vis[:h2, w1:w1 + w2, :3] = img2
    vis[50:h3 , w1 + w2:w1 + w2 + w3, :3] = img3

    cv.imshow("test", vis)
    cv.waitKey(0)