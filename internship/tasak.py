import numpy as np
import cv2
from controlled_laser import ControlledLaser

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

my_video = cv2.VideoCapture('video.mp4')
reddot = ControlledLaser((1152, 640), (1152 * 0.5, 640 * 0.5))

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('C:/Users/ozcan/Desktop/xalil_sentence/output.mp4', fourcc, 10, (1280, 720))

def find_green(img):
    global coordinates
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (29, 86, 6), (64, 255, 255))
    mask = cv2.erode(mask, np.ones((2, 1)), iterations=5)
    mask = cv2.dilate(mask, None, iterations=3)
    maskshow = mask.copy()
    maskshow = cv2.resize(maskshow, (640, 640), interpolation=cv2.INTER_AREA)

    _, cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=lambda x:cv2.contourArea(x), reverse=True)
    coordinates = [0,0]
    frame = img.copy()
    for cnt in cnts:
        if cv2.contourArea(cnt) > 2000:
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
            break

    return frame, maskshow

initial_speed = [0, 0]

while True:
    ret, my_frame = my_video.read()

    if ret == True:

        #final_speed = find_green(my_frame)
        #v_x = final_speed[0] - initial_speed[0]
        #v_y = final_speed[1] - initial_speed[1]
        #print(v_x, v_y)

        #final_frame = reddot.step(my_frame, (v_x, v_y))
        frame = find_green(my_frame)[0]
        frame = cv2.resize(frame, (640, 720), interpolation=cv2.INTER_AREA)
        frame1 = find_green(my_frame)[1]
        frame1 = cv2.resize(frame1, (640, 720), interpolation=cv2.INTER_AREA)
        frame1 = cv2.cvtColor(frame1, cv2.COLOR_GRAY2RGB)
        hori = np.concatenate((frame1, frame), axis=1)
        out.write(hori)
        #initial_speed = final_speed


        cv2.imshow('Laser Dot', hori)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    else:
        break

my_video.release()
out.release()
cv2.destroyAllWindows()