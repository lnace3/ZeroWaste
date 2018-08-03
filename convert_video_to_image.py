# Convert the video to images and store to video output
import cv2
vc = cv2.VideoCapture("dog_video.mp4")
while True:
    c = 1

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        rval, frame = vc.read()
        cv2.imwrite('video_output/' + str(c).zfill(7) + '.jpg', frame)
        c = c + 1
        cv2.waitKey()
    vc.release()
