import numpy as np
import cv2
from controlled_laser import ControlledLaser
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

my_video = cv2.VideoCapture('video.mp4')
reddot = ControlledLaser((1152, 640), (1152 * 0.5, 640 * 0.5))


def find_green(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (29, 86, 6), (64, 255, 255))
    mask = cv2.erode(mask, np.ones((2, 1)), iterations=1)
    mask = cv2.dilate(mask, None, iterations=3)
    mask = cv2.resize(mask, (640, 640), interpolation=cv2.INTER_AREA)
    cv2.imshow("mask", mask)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    frame = img.copy()
    coordinates = [0, 0, 0]
    coordinates[2] = len(cnts)
    if len(cnts) > 0:

        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 3:
            cv2.circle(frame, (int(x), int(y)), 12, (0, 255, 255), 2)
            frame = cv2.resize(frame,(640, 640),interpolation = cv2.INTER_AREA)
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.imshow("rectangle",frame)
            coordinates[0] = float(x)
            coordinates[1] = float(y)
    cv2.imshow("adasdas",frame)


    return coordinates


initial_speed = [0, 0]

while True:
    ret, my_frame = my_video.read()

    if ret == True:

        find_green(my_frame)


        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

my_video.release()
cv2.destroyAllWindows()
