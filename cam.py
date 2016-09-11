import cv2
import pickle

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
literal = vc.read()
        
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
c=0
while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    print(c)
    c += 1
cv2.destroyWindow("preview")