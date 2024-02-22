# This program is importing vehicle silhouette from .png file and save it as a numpy array in order to create an animation 

import numpy as np
import matplotlib.pyplot as plt 
import cv2
import math as m

def reduce_list(my_list, no):
    if type(my_list) is list:
        if len(my_list) == 1:
            my_list = my_list[0]
        else:
            my_list = my_list[no]
        return reduce_list(my_list, no)
    else: 
        return(my_list)



def preprocess(lr = 1.189, lf = 1.411):

    image = cv2.imread("solar.png")                      #Ładujemy JPG
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)       #nie wiem po co 

    th, image_b = cv2.threshold(src=image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)     #Tworzymy binary
    contours, hierarchy = cv2.findContours(image_b, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    #Odczytujemy contoury z binar

    cnt = contours[2]   #Konkretny contour wybieramy
    cnt_list = np.ndarray.tolist(cnt) # Zamieniam całe contours na liste zwykla

    # Array initializatioon
    x_body = []
    y_body = []
    Body_cord = []

    # Redukujemy liste do intów (floatów)
    for i in range(len(cnt_list)):
        cnt_list_temp = cnt_list[i]
        x_body.append( float(reduce_list(cnt_list_temp, 0)) )
        y_body.append( float(reduce_list(cnt_list_temp,1)) )

    # Operacje na konturze
    x_body=[(-x+800)*0.00325 for x in x_body] 
    y_body=[(-y+650)*0.00325 for y in y_body]
    x_body_n = np.array(x_body)
    y_body_n = np.array(y_body)

    Body_cord = np.vstack((x_body_n,y_body_n))
    Body_cord = np.transpose(Body_cord)

    return Body_cord
