import cv2
from threading import Thread

class webcam():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame = self.cap.read()[1]
        self.posX = 0
        self.posY = 0
        self.len = 0
        self.cascade = cv2.CascadeClassifier("E:\\Default_downloads\\open_cv\\OpenCV-master\\haarcascades\\fist.xml")
    def update(self):
        while (True):
            ret, self.frame = self.cap.read()
            self.frame = cv2.flip(self.frame, True)
            self.frame = cv2.resize(self.frame,((800,600)))
            cv2.rectangle(self.frame, (0, 0), (int(3*self.frame.shape[1] / 4), int( self.frame.shape[0] )), (0, 0, 255), 5)
            # get ROI
            roi = self.frame[5:int(self.frame.shape[0] ), 5:int(3*self.frame.shape[1] / 4), :]
            roi1 = self.frame[5:int(self.frame.shape[0] ), int(3*self.frame.shape[1] / 4):int(self.frame.shape[1]-5), :]
            # convert image to gray
            gray = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)
            gray1 = cv2.cvtColor(roi1, cv2.COLOR_RGB2GRAY)
            fist = self.cascade.detectMultiScale(gray)
            fist1 = self.cascade.detectMultiScale(gray1)
            self.len = len(fist1)
            c = []
            if len(fist) != 0:
                c = [0, 0, 0, 0]
                for x, y, w, h in fist:
                    if w * h > c[2] * c[3]:
                        c[0] = x
                        c[1] = y
                        c[2] = w
                        c[3] = h
                cv2.rectangle(self.frame, (c[0], c[1]), (c[0] + c[2], c[1] + c[3]), (0, 0, 255), 2)
                self.posX =  (c[0] + c[2]) / 2
                self.posY = (c[1] + c[3])/ 2

                # frame[y:y+h, x:x+w, :] = remask
            cv2.imshow("vid", self.frame)
            key = cv2.waitKey(30)
            if key == ord('q'):
                break

    def thread_webcam(self):
        Thread(None,self.update).start()

    def get_currentFrame(self):
        return self.frame
    def get_currentPos(self):
        return self.posX,self.posY
    def get_len(self):
        return self.len

