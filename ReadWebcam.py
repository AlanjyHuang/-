# importing required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

from imutils.video import VideoStream
from xlsxwriter import Workbook

class color:
    def run(self):
# taking the input from webcam

        plt.ion()  # Set interactive mode on

        # We will be using Video-capture to get the fps value.
        capture = cv2.VideoCapture(0)

        capture.release()

        # New module: VideoStream
        vs = VideoStream().start()

        timers = 5

        while timers>0:
            frame = vs.read()

            if frame is None:
                print("Frame is not found!")
                break
            
            b, g, r = cv2.split(frame)

            b_mean = np.mean(b)
            g_mean = np.mean(g)
            r_mean = np.mean(r)

            
            print("r:"+str(r_mean)+", g:"+str(g_mean) + ", b:" + str(b_mean))
            timers -= 1
            return list([r_mean,g_mean,b_mean])
        
if __name__ =='__main__':
        mydev=color()
        print(mydev.run())
