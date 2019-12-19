import time
import numpy as np
import cv2 as cv2
from mss import mss
from PIL import Image

# Reference for screen operations
sct = mss()

## CONSTANTS ##
MONITOR_NUMBER = 1  # 1 for 1st monitor
DEBUG = True  # True means print statements will be executed

SCREEN_TOP = 64  # does not factor in the monitor's pixel position
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240


# Use the 1st monitor
mon = sct.monitors[MONITOR_NUMBER]
monitor = {'top': mon['top'] + SCREEN_TOP, 'left': mon['left'], 'width': SCREEN_WIDTH, 'height': SCREEN_HEIGHT}

def process_image(src_img): 
    processed_img = src_img
    processed_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    # processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    # ret,thresh = cv2.threshold(processed_img,127,255,0)
    # image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return processed_img

def image_capture():
    # Frame Capture Loop
    prev_time = time.time()

    while True:
        # Get raw pixels from the screen
        sct_img = sct.grab(monitor)

        # Create the Image
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        # Process Image
        # img_array = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        img_array = np.array(img)
        img_array = process_image(img_array)

        cv2.imshow('window', img_array)

        if (DEBUG):
            curr_time = time.time()
            print("Frame took (ms) " + str(1000.0 * (curr_time - prev_time)))
            prev_time = curr_time
        
        if cv2.waitKey(30) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if (__name__ == '__main__'):
    image_capture()