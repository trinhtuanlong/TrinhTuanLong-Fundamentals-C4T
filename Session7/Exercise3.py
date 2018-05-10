from cv2 import *
from numpy import *
I = imread("D:\\GIA DINH\\LONG\\C4T2\\Lesson6\\Image\\erosion.jpg")
y = erode(I,ones((5,5),uint8))
for i in range(99):
    z = erode(y,ones((5,5),uint8))
    y = dilate(z, ones((5, 5), uint8))
ero = medianBlur(y,5)
imshow("",ero)
[r,c,ch] = ero.shape
for i in range(r):
    for j in range(c):
        ero[i,j][0] *= -110
        ero[i,j][1] *= 101
        ero[i,j][2] *= -101
imshow("",ero)
waitKey()
