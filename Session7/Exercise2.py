from cv2 import *
from numpy import *
I = imread("D:\\GIA DINH\\LONG\\C4T2\\Lesson6\\Image\\erosion.jpg")
imshow("ll",I)
ero = erode(I,ones((5,5),uint8),iterations=1)
for i in range(99):
    dil = dilate(ero,ones((5,5),uint8),iterations=1)
    ero = erode(dil,ones((5,5),uint8),iterations=1)
dil = dilate(ero,ones((5,5),uint8),iterations=1)
imshow("",dil)
waitKey()
