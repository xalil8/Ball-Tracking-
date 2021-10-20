import numpy as np
import cv2
from controlled_laser import ControlledLaser

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

my_video = cv2.VideoCapture('video.mp4')
reddot = ControlledLaser((1152, 640), (1152 * 0.5, 640 * 0.5))


def find_green(img):
    coordinates = [0, 0]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (29, 86, 6), (64, 255, 255))
    mask = cv2.erode(mask, np.ones((2, 1)), iterations=1)
    mask = cv2.dilate(mask, None, iterations=3)
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    frame = img.copy()

    if len(cnts) > 0:
        coordinates = [0, 0]
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01 "] / M["m00"]))
        if radius > 3:
            cv2.circle(frame, (int(x), int(y)), 3, (0, 255, 255), -1)
            coordinates[0] = float(x)
            coordinates[1] = float(y)
        cv2.imshow('Laser Dot', frame)
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


        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        break

my_video.release()
cv2.destroyAllWindows()