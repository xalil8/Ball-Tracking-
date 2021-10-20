import numpy as np
import cv2
from controlled_laser import ControlledLaser

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

my_video = cv2.VideoCapture('video.mp4')
reddot = ControlledLaser((1152, 640), (1152 * 0.5, 640 * 0.5))


"""def find_green(img):
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
            ((x1, y1), radius) = cv2.minEnclosingCircle(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.circle(frame, (int(x1),int(y1)), 5, (0, 0, 255), -1)
            break

    return frame"""

def find_green(img):
    coordinates = [0, 0]

    blurred = cv2.GaussianBlur(img, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    erosion = cv2.erode(mask, np.ones((11, 11)), iterations=1)
    dilate = cv2.dilate(erosion, np.ones((11, 11)), iterations=1)
    _, contour, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = sorted(contour, key=lambda t: cv2.contourArea(t), reverse=True)
    cv2.imshow('Laser Dot', dilate)
    for cnt in contour:
        if cv2.contourArea(cnt) > 200:
            ((x, y), radius) = cv2.minEnclosingCircle(cnt)
            M = cv2.moments(cnt)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius > 10:
                cv2.circle(img, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(img, center, 5, (0, 0, 255), -1)

            coordinates[0] = x
            coordinates[1] = y
            print(coordinates)
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