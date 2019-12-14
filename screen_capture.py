# import numpy as np
# import pyscreenshot as ImageGrab
# # from PIL import ImageGrab
# import cv2
# import time

# def screen_record(): 
#     last_time = time.time()
#     while(True):
#         # 800x600 windowed mode for GTA 5, at the top left position of your main screen.
#         # 40 px accounts for title bar. 
#         printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
#         print('loop took {} seconds'.format(time.time()-last_time))
#         last_time = time.time()
#         cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
#         # if cv2.waitKey(25) & 0xFF == ord('q'):
#         #     cv2.destroyAllWindows()
#         #     break

# screen_record()



import numpy as np
import cv2
from mss import mss
from PIL import Image

mon = {'top': 160, 'left': 160, 'width': 200, 'height': 200}
# mon = (160, 160, 200, 200)

sct = mss()
# Use the 1st monitor
monitor = sct.monitors[1]

while True:
    # Get raw pixels from the screen
    sct_img = sct.grab(monitor)

    # Create the Image
    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    
    cv2.imshow('test', np.array(img))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break