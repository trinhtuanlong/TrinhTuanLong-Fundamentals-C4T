from cv2 import *
from numpy import *
class ShapeDetector:
    def __init__(self): pass
    def detect(self,c):
        shape = "unidentified"
        peri = arcLength(c,True)
        approx = approxPolyDP(c, 0.03 * peri, True)
        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        elif len(approx) == 5:
            shape = "pentagon"
        else:
            shape = "circle"
        return shape
I = imread("D:\\GIA DINH\\LONG\\C4T2\\Lesson6\\Image\\ggg.png")
ratio = 1
gray = cvtColor(I, cv2.COLOR_BGR2GRAY)
blurred = GaussianBlur(gray, (5, 5), 0)
ret,thresh = threshold(blurred, 200, 255, THRESH_BINARY_INV)
imshow("88", thresh)
cont,cnts,hie = findContours(thresh.copy(),RETR_EXTERNAL,CHAIN_APPROX_NONE)
drawContours(I, cnts, -1, (0, 255, 0), 15)
imshow("rrr",I)
sd = ShapeDetector()
for c in cnts:
    M = moments(c)
    cX = int((M["m10"] / M["m00"])*ratio)
    cY = int((M["m01"] / M["m00"])*ratio)
    shape = sd.detect(c)
    putText(I, shape, (cX, cY), FONT_HERSHEY_SIMPLEX,0.55, (255, 255, 255), 2)
imshow("Image", I)
waitKey(0)