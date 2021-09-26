import cv2 as cv;
import sys;
import numpy;

print(numpy.__file__)

img = cv.imread(cv.samples.findFile("resources/tommy.png"))

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Image Window", img)

k = cv.waitKey(0)