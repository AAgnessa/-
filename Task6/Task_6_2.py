import cv2
import numpy as np

photo=cv2.imread('Task6/photo.jpg')

def show_clicked(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(photo, (x,y), 5, (255,0,0), 2)
 
cv2.namedWindow(winname='this_window')
cv2.setMouseCallback('this_window', show_clicked)
while True:
    cv2.imshow('this_window', photo)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()