import cv2
import numpy as np
import matplotlib.pyplot as plt

from imutils.video import VideoStream
from xlsxwriter import Workbook

fig = plt.figure()

plt.ion()  # Set interactive mode on

# We will be using Video-capture to get the fps value.
capture = cv2.VideoCapture(0)
fps = capture.get(cv2.CAP_PROP_FPS)
capture.release()

# New module: VideoStream
vs = VideoStream().start()

is_new_frame = False

while True:
    frame = vs.read()

    if frame is None:
        print("Frame is not found!")
        break
    
    b, g, r = cv2.split(frame)

    print("r:"+str(r)+", g:"+str(g) + ", b:" + str(b))

#     if frame_count % int(fps) == 0:

#         is_new_frame = True  # New frame has come

#         line = [line for line in zip(b, g, r) if len(line)]

#         s_frame.append(second)
#         b_frame.append(np.mean(line[0]) * 0.02)
#         g_frame.append(np.mean(line[1]) * 0.03)
#         r_frame.append(np.mean(line[2]) * 0.04)

#         plt.plot(s_frame, b_frame, 'b', label='blue', lw=7)
#         plt.plot(s_frame, g_frame, 'g', label='green', lw=4)
#         plt.plot(s_frame, r_frame, 'r', label='red')
#         plt.xlabel('seconds')
#         plt.ylabel('mean')
#         if frame_count == 0:
#             plt.legend()
#         plt.show()

#         second += 1

#     elif second > 2:

#         if is_new_frame:

#             if second == 3:
#                 blue.extend(b_frame)
#                 green.extend(g_frame)
#                 red.extend(r_frame)
#                 xs.extend(s_frame)
#             else:
#                 blue.append(b_frame[len(b_frame)-1])
#                 green.append(g_frame[len(g_frame)-1])
#                 red.append(r_frame[len(r_frame)-1])
#                 xs.append(s_frame[len(s_frame)-1])

#             del b_frame[0]
#             del g_frame[0]
#             del r_frame[0]
#             del s_frame[0]

#             is_new_frame = False  # we added the new frame to our list structure

#     cv2.imshow('Frame', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#     frame_count += 1

# cv2.destroyAllWindows()
# capture.release()
# vs.stop()

# book = Workbook('Channel.xlsx')
# sheet = book.add_worksheet()

# row = 0
# col = 0

# sheet.write(row, col, 'Seconds')
# sheet.write(row + 1, col, 'Blue mean')
# sheet.write(row + 2, col, 'Green mean')
# sheet.write(row + 3, col, 'Red mean')

# col += 1

# for s, b, g, r in zip(xs, blue, green, red):
#     sheet.write(row, col, s)
#     sheet.write(row + 1, col, b)
#     sheet.write(row + 2, col, g)
#     sheet.write(row + 3, col, r)
#     col += 1

# book.close()