import numpy as np
import cv2
from controlled_laser import ControlledLaser

my_video = cv2.VideoCapture('video.mp4')
red_dot = ControlledLaser((1152, 640), (350, 610))

final_speed = [0, 0]
coordinates = [0, 0]
initial_speed = [0, 0]
subs_speed = [0, 0]

while True:

    ret, my_frame = my_video.read()
    if ret:

        hsv = cv2.cvtColor(my_frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (29, 86, 6), (64, 255, 255))
        _, contour, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour = sorted(contour, key=lambda t: cv2.contourArea(t), reverse=True)

        frame = my_frame.copy()
        for cnt in contour:
            if cv2.contourArea(cnt) > 200:
                ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 0, 255), 2)
                M = cv2.moments(cnt)
                c_x = int(M['m10'] / M['m00'])
                c_y = int(M['m01'] / M['m00'])
                final_speed[0] = c_x
                final_speed[1] = c_y
                break

        if final_speed[0] == 0 and final_speed[1] == 0:

            final_frame = my_frame
            initial_speed = subs_speed
        else:
            vx = final_speed[0] - initial_speed[0]
            vy = final_speed[1] - initial_speed[1]

            final_frame = red_dot.step(my_frame, (vx, vy))
            initial_speed = final_speed
            subs_speed = final_speed

        cv2.imshow('Laser Dot', final_frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        break
my_video.release()
cv2.destroyAllWindows()
