import cv2
import numpy as np

my_video = cv2.VideoCapture("input.mov")


def processing(img):

    blurred = cv2.blur(img, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    erosion = cv2.erode(hsv, np.ones((11, 11)), iterations=1)
    dilate = cv2.dilate(erosion, np.ones((11, 11)), iterations=1)
    th = cv2.adaptiveThreshold(dilate, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    cv2.imshow("deneme", th)

def alpfunction(img):

    img = cv2.medianBlur(img, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, 0.9, 120, param1=50, param2=30, minRadius=60, maxRadius=120)

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow('detected circles', cimg)


while True:
    _, my_frame = my_video.read()

    if _:
        height, width, layers = my_frame.shape
        new_h = height / 2
        new_w = width / 2
        resize = cv2.resize(my_frame, (int(new_w), int(new_h)))

        processing(resize)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        break
my_video.release()
cv2.destroyAllWindows()

