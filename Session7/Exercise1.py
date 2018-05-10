# from cv2 import *
# from numpy import *
# I = imread("D:\\GIA DINH\\LONG\\C4T2\\Lesson6\\Image\\Lenna.png")
# gray = cvtColor(I,COLOR_RGB2GRAY)
# ret,bin = threshold(gray,127.5,255,THRESH_BINARY)
# imshow("",bin)
# waitKey()
import numpy as np
import cv2

# Load Image RGB
I = cv2.imread("D:\\GIA DINH\\LONG\\C4T2\\Lesson6\\Image\\shape.jpg")
cv2.imshow("I", I);
cv2.waitKey()
# convert Whiter color to black
[rows, cols, c] = I.shape;
for i in range(rows):
    for j in range(cols):
        if I[i,j,0] >200 and I[i,j,1] >200 and I[i,j,2] >200 :
            I[i,j,:] = 0;
cv2.imshow("Inew", I);
cv2.waitKey()
# Extract chanel B
B = I[:,:,0]
# Extract chanel G
G = I[:,:,1]
# Extract chanel R
R = I[:,:,2]
# Thresold for chanel B
threshB,binB = cv2.threshold(B,100,255,cv2.THRESH_BINARY)
cv2.imshow("B",binB)
threshG,binG = cv2.threshold(G,100,255,cv2.THRESH_BINARY)
cv2.imshow("G",binG)
threshR,binR = cv2.threshold(R,100,255,cv2.THRESH_BINARY)
cv2.imshow("R",binR)
cv2.imshow("binaryImage", binR+binB+binG);
cv2.waitKey()
# I = cv2.imread("D:\\GIA DINH\\LONG\\C4T2\\Lesson6\\Image\\test2.png")
# cv2.imshow("I", I);
# cv2.waitKey()
# # convert Whiter color to black
# [rows, cols, c] = I.shape;
# for i in range(rows):
#     for j in range(cols):
#         if I[i,j,0] >200 and I[i,j,1] >200 and I[i,j,2] >200 :
#             I[i,j,:] = 0;
# cv2.imshow("Inew", I);
# cv2.waitKey()
# # Extract chanel B
# B = I[:,:,0]
# # Extract chanel G
# G = I[:,:,1]
# # Extract chanel R
# R = I[:,:,2]
# # Thresold for chanel B
# threshB,binB = cv2.threshold(B,100,255,cv2.THRESH_BINARY)
# cv2.imshow("B",binB)
# threshG,binG = cv2.threshold(G,100,255,cv2.THRESH_BINARY)
# cv2.imshow("G",binG)
# threshR,binR = cv2.threshold(R,100,255,cv2.THRESH_BINARY)
# cv2.imshow("R",binR)
# cv2.imshow("binaryImage", binR+binB+binG);
# cv2.waitKey()
