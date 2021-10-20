import cv2
import numpy as np
import imutils
img = cv2.imread("dataset/detect2.jpeg")
resized = cv2.resize(img, (640,480), interpolation=cv2.INTER_AREA)


grey_imag = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)


def another_func(raw):
    image = raw
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # perform edge detection
    edges = cv2.Canny(grayscale, 30, 100)
    # detect lines in the image using hough lines technique
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)
    # iterate over the output lines and draw them
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
            cv2.line(edges, (x1, y1), (x2, y2), (255, 0, 0), 3)
    # show images
    cv2.imshow("image", image)
    cv2.imshow("edges", edges)


def deneme(image):
    gaussian = cv2.GaussianBlur(image, (11, 11), 0)
    erosion1 = cv2.erode(gaussian, np.ones((5, 5)), iterations=1)
    dilate1 = cv2.dilate(erosion1, np.ones((5, 5)), iterations=1)
    ret, thresh_img = cv2.threshold(dilate1, 100, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_contours = np.zeros((480,640,3), np.uint8)
    cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)

    edges = cv2.Canny(image, 30, 100)
    # detect lines in the image using hough lines technique
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)
    # iterate over the output lines and draw them
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
            cv2.line(edges, (x1, y1), (x2, y2), (255, 0, 0), 3)


    cv2.imshow("gaussian", image)

    median = cv2.medianBlur(image, 9)
    erosion2 = cv2.erode(median, np.ones((5, 5)), iterations=1)
    dilate2 = cv2.dilate(erosion2, np.ones((5, 5)), iterations=1)



    bilateral = cv2.bilateralFilter(image, 11, 17, 17)
    erosion3 = cv2.erode(bilateral, np.ones((5, 5)), iterations=1)
    dilate3 = cv2.dilate(erosion3, np.ones((5, 5)), iterations=1)

    circles = cv2.HoughCircles(dilate2, cv2.HOUGH_GRADIENT, 1, img.shape[0] / 64, param1=200, param2=10, minRadius=5,
                               maxRadius=300)

    edged = cv2.Canny(bilateral, 30, 200)



    cv2.imshow("mediam", circles)
    cv2.imshow("bilateral", dilate3)

another_func(img)
"""erosion = cv2.erode(hsv, np.ones((11, 11)), iterations=1)
dilate = cv2.dilate(erosion, np.ones((11, 11)), iterations=1)
edges = cv2.Canny(dilate, 100, 200)
#th = cv2.adaptiveThreshold(dilate, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval, threshold1 = cv2.threshold(hsv, 12, 255, cv2.THRESH_BINARY)

gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
cv2.imshow('plain', dilate)
cv2.imshow("deneme", edges)

"""

cv2.waitKey(0)
