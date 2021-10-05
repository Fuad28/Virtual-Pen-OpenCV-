import cv2
import numpy as np
from funcs import getContours, stackImages

myColors= [
    
    [57, 76, 0, 100, 255, 255], #green
    [0, 0, 25, 179, 255, 40] #Black
]

myColorValues= [
  
    [0, 255, 0], #Green
    [0, 0, 0] #Black
]

myPoints= [] # [x, y, colorId]

def getContours(img, imgContour):
    contours, hierarchy=  cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y, w, h= (0,0,0,0)
    for cnt in contours:
        if area:= cv2.contourArea(cnt) > 500:
            #cv2.drawContours(imgContour, cnt, -1, (255, 0, 0 ), 3)
            perimeter= cv2.arcLength(cnt, True)
            approx= cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            x, y, w, h= cv2.boundingRect(approx)
    return x+w//2, y



def findColors(img, imgResult, myColorsHSV, myColorsBGR):
    imgHSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
    newPoints= []
    for count, color in enumerate(myColorsHSV):
        lower= np.array(color[0:3])
        upper= np.array(color[3:6])
        mask= cv2.inRange(imgHSV, lower, upper)
        x, y= getContours(mask, imgResult)

        if x!=0 and y!=0:
            cv2.circle(imgResult, (x, y), 10, myColorsBGR[count], cv2.FILLED)
            newPoints.append([x, y, count])
    return newPoints


def drawOnCanvas(myPoints, myColorRGB):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorRGB[point[2]], cv2.FILLED)



cap= cv2.VideoCapture(1)
frameWidth, frameHeight= 320, 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

while True:
    success, img= cap.read()
    imgResult= img.copy()
    newPoints=  findColors(img, imgResult, myColors, myColorValues)

    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)


    cv2.imshow('Result', imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
