import numpy as np
import cv2
from controlled_laser import ControlledLaser
"""cv2.namedWindow("dot",cv2.WINDOW_NORMAL)
cv2.namedWindow("mask",cv2.WINDOW_NORMAL)
cv2.namedWindow("rectangle",cv2.WINDOW_NORMAL)"""
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

my_video = cv2.VideoCapture('video.mp4')
reddot = ControlledLaser((1152, 640), (606, 633))


def find_green(img):
    global coordinates
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (29, 86, 6), (64, 255, 255))
    mask = cv2.resize(mask, (640, 640), interpolation=cv2.INTER_AREA)
    cv2.imshow("mask", mask)
    _, cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=lambda x:cv2.contourArea(x), reverse=True)
    coordinates = [0,0]
    frame = img.copy()
    for cnt in cnts:
        if cv2.contourArea(cnt) > 2000:
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            frame = cv2.resize(frame,(640, 640),interpolation = cv2.INTER_AREA)
            cv2.imshow("rectangle",frame)
            coordinates = x, y
            break

    return coordinates

initial_speed = [606, 633]

while True:
    ret, my_frame = my_video.read()
    #my_frame = cv2.resize(my_frame, (0, 0), None, .25, .25)
    if ret == True:

        final_speed = find_green(my_frame)
        v_x = final_speed[0] - initial_speed[0]
        v_y = final_speed[1] - initial_speed[1]
        final_frame = reddot.step(my_frame, (v_x, v_y))
        initial_speed = final_speed
        final_frame = cv2.resize(final_frame, (640, 640), interpolation=cv2.INTER_AREA)
        cv2.imshow('dot', final_frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

my_video.release()
cv2.destroyAllWindows()
