# This is stage 1 of 3 in the Puzzle Cheat Sheet Project
# Code was created following the tutorial https://www.youtube.com/watch?v=DaQoorJQSZQ&list=PLMoSUbG1Q_r_sc0x7ndCsqdIkL7dwrmNF&index=8
# Zuggyg 03/06/21

import cv2
import numpy as np

print("hello")

#global variables
circles = np.zeros((4,2), np.int)
ccounter = 0
#path of Image
path = r'original.jpg'

#function that does something on mouseclick
def mousePoints(event,x,y,flags,paramas):
    #make sure to enter this to use the global variables within a function
    global ccounter
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        circles[ccounter] = x,y
        print(circles)
        ccounter = ccounter + 1

#function that calls the image to be marked
def imagetomark():
        #draw circles on the corners
        for x in circles:
            cv2.circle(img,(int(x[0]),int(x[1])),5,(0,0,255),cv2.FILLED)
        #display image
        cv2.imshow("Original Image", img)
        #allow image window to be clicked on. First paramater is the image window, second paramater is the function to feed the mouse info into
        cv2.setMouseCallback("Original Image", mousePoints)
        cv2.waitKey(100)


#read the image from file
img = cv2.imread(path)

#loops on original image until there are 4 clicks
myloop = 1
while myloop == 1:
    imagetomark()
    if ccounter == 4:
        myloop = 2

#once 4 clicks are registered it processes the image and then displays result
if ccounter == 4:
    imagetomark()
    #reread original image so have clean plate
    img = cv2.imread(path)
    #create output dimensions
    width, height = 490, 360
    pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    #do the deskewing magic
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv2.warpPerspective(img,matrix,(width,height))
    cv2.imshow("Output Image", imgOutput)
    cv2.waitKey(0)
    #save image
    cv2.imwrite(r'deskewed.jpg', imgOutput)

print("completed")
