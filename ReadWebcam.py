# importing required libraries
import cv2
import numpy as np
import time
class color:
    def run(self):
# taking the input from webcam
        vid = cv2.VideoCapture(0)

        timers = 5

# running while loop just to make sure that
# our program keep running untill we stop it
        while timers>0:

            # capturing the current frame
            _, frame = vid.read()

            # displaying the current frame
            #cv2.imshow("frame", frame)

            # setting values for base colors
            b = frame[:, :, :1]
            g = frame[:, :, 1:2]
            r = frame[:, :, 2:]

            # computing the mean
            b_mean = np.mean(b)
            g_mean = np.mean(g)
            r_mean = np.mean(r)



            print("r:" + str(r_mean) + ",g:" + str(g_mean) + ",b:" + str(b_mean))

                # displaying the most prominent color
            if (b_mean > g_mean and b_mean > r_mean):
                print("Blue")
            if (g_mean > r_mean and g_mean > b_mean):
                print("Green")
            else:
                print("Red")

            time.sleep(1)
            timers -= 1
            return ("r:" + str(r_mean) + ",g:" + str(g_mean) + ",b:" + str(b_mean))
