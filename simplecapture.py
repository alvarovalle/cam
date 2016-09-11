import cv2
import pickle

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
literal = vc.read()
with open('cam_data.pkl', 'wb') as output:
  pickle.dump(literal, output, pickle.HIGHEST_PROTOCOL)

close('cam_data.pkl')        
