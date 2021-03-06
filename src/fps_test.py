import sys, time
import cv2 as cv
import numpy as np
from mss import mss
from settings import Settings
from setup import setup
import pyautogui as pag


config = Settings()
setup(config)

with mss() as sct:
  # Part of the screen to capture
  # monitor = {"top": 0, "left": 0, "width": 1000, "height": 570}
  monitor = config.get_monitor()
  print(monitor)
  while "Screen capturing":
    last_time = time.time()

    # Get raw pixels from the screen, save it to a Numpy array
    img = np.array(sct.grab(monitor))

    # Display the picture
    cv.imshow("OpenCV/Numpy normal", img)

    # Display the picture in grayscale
    # cv2.imshow('OpenCV/Numpy grayscale',
    #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

    print("fps: {}".format(1 / (time.time() - last_time)))
    print(pag.position())

    # Press "q" to quit
    if cv.waitKey(25) & 0xFF == ord("q"):
      cv.destroyAllWindows()
      break