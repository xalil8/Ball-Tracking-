import numpy as np
import easyocr
import cv2
import math
import tiffile

def goruntuisleme():
    print("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")

    cv2.namedWindow("showup",cv2.WINDOW_NORMAL)
    cv2.namedWindow('controls',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('controls',850,250)
    cv2.resizeWindow('showup',850,250)



    cv2.createTrackbar('Blur','controls',9,20,lambda x:x)
    cv2.createTrackbar('Blur Iteration','controls',0,10,lambda x:x)
    cv2.createTrackbar('Threshold Block Size','controls', 80, 255, lambda x:x)
    cv2.createTrackbar('Threshold Constant','controls', 180, 255, lambda x:x)
    cv2.createTrackbar('Erosion Kernel Size','controls', 1, 20, lambda x:x)
    cv2.createTrackbar('Erosion Iteration','controls',1, 10, lambda x:x)
    cv2.createTrackbar('Dilation Kernel Size','controls', 1, 20, lambda x:x)
    cv2.createTrackbar('Dilation Iteration','controls', 1, 10, lambda x:x)
    cv2.createTrackbar('Threshold Flag','controls', 5, 5, lambda x:x)
    cv2.createTrackbar('BITWISE ON OFF','controls', 0, 1, lambda x:x)
    cv2.createTrackbar('ADAPTIVE TO NORMAL THRESHOLD','controls', 0, 1, lambda x:x)

    #img = cv2.imread("/home/xalil8/imwrites/eng.gorton.exp2.png")
    img = cv2.imread("50dolar.jpg")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #img = cv2.imread("/home/xalil8/Desktop/img.tiff", cv2.IMREAD_GRAYSCALE)

    def th_key_maker(key):

        if key == 1:
            print("cv2.THRESH_BINARY_INV")
            return cv2.THRESH_BINARY_INV
        elif key == 2:
            print("cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU")
            return cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        elif key == 3:
            print("cv2.THRESH_TOZERO")
            return cv2.THRESH_TOZERO
        elif key == 4:
            print("cv2.THRESH_TOZERO_INV")
            return cv2.THRESH_TOZERO_INV
        elif key == 5:
            print("cv2.THRESH_TRUNC")
            return cv2.THRESH_TRUNC
        else:
            print("cv2.THRESH_BINARY")
            return cv2.THRESH_BINARY

    counter = 2

    while True:


        blur = int(cv2.getTrackbarPos('Blur', 'controls'))
        blur_it = int(cv2.getTrackbarPos('Blur Iteration', 'controls'))
        th1 = int(cv2.getTrackbarPos('Threshold Block Size', 'controls'))
        th2 = int(cv2.getTrackbarPos('Threshold Constant', 'controls'))
        eksize = int(cv2.getTrackbarPos('Erosion Kernel Size', 'controls'))
        eit = int(cv2.getTrackbarPos('Erosion Iteration', 'controls'))
        dksize = int(cv2.getTrackbarPos('Dilation Kernel Size', 'controls'))
        dit = int(cv2.getTrackbarPos('Dilation Iteration', 'controls'))
        th_key_num = int(cv2.getTrackbarPos('Threshold Flag', 'controls'))
        bitwise_on_off = int(cv2.getTrackbarPos('BITWISE ON OFF', 'controls'))
        adaptive_to_normal = int(cv2.getTrackbarPos('ADAPTIVE TO NORMAL THRESHOLD', 'controls'))




        th_key = th_key_maker(th_key_num)


        while blur % 2 == 0 or blur <3:
            blur += 1

        while th1 % 2 == 0 or th1 < 2:
            th1 += 1

        while th2 % 2 == 0:
            th2 += 1

        #blurred = cv2.medianBlur(img,blur)
        blurred = cv2.GaussianBlur(img, (blur, blur), blur_it)
        #blurred = cv2.GaussianBlur(img, (blur, blur), blur_it)

        if adaptive_to_normal:
            qret, threshold = cv2.threshold(blurred, th1, th2, th_key)
            #ret, threshold = cv2.threshold(blurred, th1, th2, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        else:
            threshold = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,th1,th2)


        if bitwise_on_off:
            bitwise = cv2.bitwise_not(threshold)
        else:
            bitwise = threshold


        erosion = cv2.erode(bitwise, (eksize,eksize), eit)
        dilate = cv2.dilate(erosion,(dksize, dksize), dit)

        cannied = cv2.Canny(dilate, 50, 200, None, 3)
        lines = cv2.HoughLines(cannied, 1, np.pi / 180, 150, None, 0, 0)
        if lines is not None:
            for i in range(0, len(lines)):
                rho = lines[i][0][0]
                theta = lines[i][0][1]
                a = math.cos(theta)
                b = math.sin(theta)
                x0 = a * rho
                y0 = b * rho
                pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
                pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
                cv2.line(img, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)

        cv2.imshow("showup", img)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            print("dataset" + str(counter) + ".png saving")

            #tifffile.imwrite("C:/Users/ozcan/Desktop/dataset-tiff/testlan.gorton.exp" + str(counter) + ".tiff", dilate)
            #cv2.imwrite("/home/xalil8/imwrites/eng.gorton.exp" + str(counter) + ".png", threshold)
            cv2.imwrite("C:/Users/ozcan/Desktop/letter_dataset/letter" + str(counter) + ".png", dilate)


            counter = counter + 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()



#print("code done ")

#goruntuisleme()




"""def ocr():
    image_path = 
"""


"""save = input("enter 's' if you wanna save\n ")


if save == "s":

    data_num = input("enter data number")
    print("eng.gorton.exp" + str(data_num) + ".png    saving ")q
    cv2.imwrite("C:/Users/ozcan/Desktop/xalil-dataset/eng.gorton.exp" + str(data_num) + ".tiff", dilate)
"""

def line():
    cv2.namedWindow("showup", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('showup',850,250)
    img = cv2.imread("50dolar.jpg")
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cannied = cv2.Canny(img, 50, 200, None, 3)
    lines = cv2.HoughLines(cannied, 1, np.pi / 180, 150, None, 0, 0)
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(img, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)

    cv2.imshow("showup", cannied)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


line()