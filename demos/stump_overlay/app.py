import cv2 as cv;
import sys;

sample_video_path = "D:\Films\cricket footage\MVI_2654.mp4"
sample_image_path = "resources/tommy.png"

def showImage(path):
    img = cv.imread(cv.samples.findFile(path))
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow("Image Window", img)

def showVideo(path):
    vid = cv.VideoCapture(path)
    
    while vid.isOpened():
        ret, frame = vid.read()

        if not ret:
            print("Can't receive frame (end of video?). Exiting...")
            break
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break


showVideo(sample_video_path)