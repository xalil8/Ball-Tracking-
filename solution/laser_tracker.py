import numpy as np
import cv2
from controlled_laser import ControlledLaser

green_lower = np.array([29, 86, 6]) # lower value for green color
green_upper = np.array([64, 255, 255])  # upper value for green color
my_video = cv2.VideoCapture('video.mp4')   # getting video
red_dot = ControlledLaser((1152, 640), (606, 633))  # creating laser instance
initial_coordinates = (606, 633)
# i took that point as an initial because of red ball first time show up in this location


def find_green(img):  # function which take image as a parameter then return center coordinates of ball
    ball_coordinates = [-1, -1]
    # image processing and filters
    blurred = cv2.blur(img, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, green_lower, green_upper)
    erosion = cv2.erode(mask, np.ones((11, 11)), iterations=1)
    dilate = cv2.dilate(erosion, np.ones((11, 11)), iterations=1)
    _, contour, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = sorted(contour, key=lambda t: cv2.contourArea(t), reverse=True)
    newimg = img.copy()
    for cnt in contour:
        area = cv2.contourArea(cnt)
        if cv2.contourArea(cnt) > 1000:  # to eliminate smallest green areas except ball
            ((x, y), radius) = cv2.minEnclosingCircle(cnt)  # minimum enclosing circle of ball
            cv2.circle(newimg,(int(x),int(y)),int(radius),(0,0,255),1)
            cv2.circle(dilate, (int(x), int(y)), int(radius), (0, 0, 255), 1)

            M = cv2.moments(cnt)   # find center of mass of ball to get coordinates of those points
            c_x = float(M['m10'] / M['m00'])
            c_y = float(M['m01'] / M['m00'])
            cv2.circle(newimg, (int(c_x), int(c_y)), int(radius), (255, 0, 0), 1)
            ball_coordinates = c_x, c_y  # initializing ball center coordinates in a list
            #print(x,y,"----------",int(c_x),int(c_y))
            cv2.imshow("yarak", newimg)

    cv2.imshow("asdasd",dilate)
     # return coordinates


while True:
    counter, my_frame = my_video.read()  # getting frames from video

    if counter:  # this value turn True if we can get frame then loop work



        find_green(my_frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

my_video.release()
cv2.destroyAllWindows()
