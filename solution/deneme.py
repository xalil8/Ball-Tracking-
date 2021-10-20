import numpy as np
import cv2
from controlled_laser import ControlledLaser

green_lower = np.array([29, 86, 6]) # lower value for green color
green_upper = np.array([64, 255, 255])
my_video = cv2.VideoCapture('video.mp4')   # getting video
red_dot = ControlledLaser((1152, 640),(606, 633))  # creating laser instance
initial_coordinates = (606, 633)
final_coordinates = (0, 0)
object_detector = cv2.createBackgroundSubtractorMOG2()

while True:
    counter, my_frame = my_video.read()

    if counter:
        blurred = cv2.blur(my_frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)  # change color space rgb to hsv to process image
        mask = cv2.inRange(hsv, green_lower, green_upper)
        erosion = cv2.erode(mask, np.ones((5, 5)), iterations=2)
        dilate = cv2.dilate(erosion, np.ones((5, 5)), iterations=2)-

        cv2.imshow("yarak", median)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    else:
        break

my_video.release()
cv2.destroyAllWindows()
