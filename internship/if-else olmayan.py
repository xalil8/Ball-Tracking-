import numpy as np
import cv2
from controlled_laser import ControlledLaser

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

my_video = cv2.VideoCapture('video.mp4')
reddot = ControlledLaser((1152, 640), (350, 610))


def find_green(img):
    global coordinates
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (29, 86, 6), (64, 255, 255))
    _, cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=lambda x:cv2.contourArea(x), reverse=True)
    coordinates = [0,0]
    frame = img.copy()
    for cnt in cnts:
        if cv2.contourArea(cnt) > 2000:
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            coordinates = x, y
            break

    return coordinates

initial_speed = [0, 0]

while True:
    ret, my_frame = my_video.read()

    if ret == True:

        final_speed = find_green(my_frame)
        v_x = final_speed[0] - initial_speed[0]
        v_y = final_speed[1] - initial_speed[1]
        print(v_x, v_y)

        final_frame = reddot.step(my_frame, (v_x, v_y))

        initial_speed = final_speed

        cv2.imshow('Laser Dot', final_frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        break

my_video.release()
cv2.destroyAllWindows()
