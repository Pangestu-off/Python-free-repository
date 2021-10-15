import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture('Animasi640.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 540)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cv2.namedWindow('Trackbar')

cv2.createTrackbar("L - H","Trackbar", 0, 255, nothing)
cv2.createTrackbar("L - S","Trackbar", 174, 255, nothing)
cv2.createTrackbar("L - V","Trackbar", 11, 255, nothing) 
cv2.createTrackbar("U - H","Trackbar", 255, 255, nothing)
cv2.createTrackbar("U - S","Trackbar", 255, 255, nothing)
cv2.createTrackbar("U - V","Trackbar", 255, 255, nothing)

while True:
    _,frame = cap.read(1)

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)
    l_h = cv2.getTrackbarPos("L - H", "Trackbar") #trackbar data
    l_s = cv2.getTrackbarPos("L - S", "Trackbar")   #trackbar data
    l_v = cv2.getTrackbarPos("L - V", "Trackbar")   #trackbar data
    u_h = cv2.getTrackbarPos("U - H", "Trackbar")   #trackbar data
    u_s = cv2.getTrackbarPos("U - S", "Trackbar")   #trackbar data
    u_v = cv2.getTrackbarPos("U - V", "Trackbar")   #trackbar data
    lower_oren = np.array([l_h,l_s,l_v])
    upper_oren = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, lower_oren, upper_oren)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    key = cv2.waitKey(1)
    if key == 27:
        break
