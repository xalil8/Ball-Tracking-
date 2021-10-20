import cv2
import numpy as np
import random
from PIL import Image, ImageOps


# her çalıştığında girdiniz letter sayısı uzunluğunda (2-7 harf arası ) kelime üretiyor
def word_maker():
    num_of_let = 6
    empty_matrix_color = 0
    oversize = 100
    add_size = int(oversize / 2)
    image_list = [0,1,2,3,4,5]
    image_list[0] = image = cv2.imread("letters_new/B.png")
    image_list[1] = image = cv2.imread("letters_new/left_parentheses.png")
    image_list[2] = image = cv2.imread("letters_new/low_g.png")
    image_list[3] = image = cv2.imread("letters_new/2.png" )
    image_list[4] = image = cv2.imread("letters_new/coma.png")
    image_list[5] = image = cv2.imread("letters_new/low_p.png")


    if num_of_let == 6:
        h1, w1 = image_list[0].shape[0:2]
        h2, w2 = image_list[1].shape[0:2]
        h3, w3 = image_list[2].shape[0:2]
        h4, w4 = image_list[3].shape[0:2]
        h5, w5 = image_list[4].shape[0:2]
        h6, w6 = image_list[5].shape[0:2]

        h_key = 480
        h_max  = max(h1, h2, h3, h4, h5, h6)
        vis = np.zeros((h_key, w1 + w2 + w3 + w4 + w5 + w6, 3), np.uint8)
        vis.fill(empty_matrix_color)

        g_adjust = 60
        pad_thick = 125

        vis[h_key-h1-pad_thick:h_key-pad_thick,:w1, :3] = image_list[0]
        vis[h_key-h2-pad_thick:h_key-pad_thick, w1:w1 + w2, :3] = image_list[1]
        vis[h_key-h3-pad_thick+g_adjust:h_key-pad_thick+g_adjust, w1 + w2:w1 + w2 + w3, :3] = image_list[2]
        vis[h_key-h4-pad_thick:h_key-pad_thick, w1 + w2 + w3:w1 + w2 + w3 + w4 , :3] = image_list[3]
        vis[h_key-h5-pad_thick:h_key-pad_thick, w1 + w2 + w3 + w4:w1 + w2 + w3 + w4 + w5, :3] = image_list[4]
        vis[h_key-h6-pad_thick+g_adjust:h_key-pad_thick+g_adjust, w1 + w2 + w3 + w4 + w5 :w1 + w2 + w3 + w4 + w5 + w6, :3] = \
        image_list[5]


        img_pad = cv2.copyMakeBorder(vis, 0, 0, 0, 50, 1,(0,0,0))

        return img_pad






def sentence_maker(number_of_words=1):
    words_list = []

    for i in range(number_of_words):
        word = word_maker()
        words_list.append(word)

    if number_of_words == 1:
        vis = words_list[0]
        vis = cv2.flip(vis, -1)
        return vis


    elif number_of_words == 2:

        h1, w1 = words_list[0].shape[0:2]
        h2, w2 = words_list[1].shape[0:2]
        vis = np.zeros((max(h1, h2), w1 + w2, 3), np.uint8)
        vis.fill(177)

        vis[:h1, :w1, :3] = words_list[0]
        vis[:h2, w1:w1 + w2, :3] = words_list[1]
        vis = cv2.flip(vis, -1)
        return vis


    elif number_of_words == 3:
        h1, w1 = words_list[0].shape[0:2]
        h2, w2 = words_list[1].shape[0:2]
        h3, w3 = words_list[2].shape[0:2]

        vis = np.zeros((max(h1, h2, h3), w1 + w2 + w3, 3), np.uint8)
        vis.fill(255)

        vis[:h1, :w1, :3] = words_list[0]
        vis[:h2, w1:w1 + w2, :3] = words_list[1]
        vis[:h3, w1 + w2:w1 + w2 + w3, :3] = words_list[2]
        vis = cv2.flip(vis, -1)
        return vis




def write_data(number_of_image):
    list1 = []

    for i in range(number_of_image):
        data = sentence_maker(random.randrange(1, 4))
        cv2.imwrite(f"C:/Users/ozcan/Desktop/dataset_for_robot/sentence{str(i)}.png", data)

    print("All process Done")


cv2.imshow("deneme",word_maker())
cv2.waitKey(0)
cv2.destroyAllWindows()