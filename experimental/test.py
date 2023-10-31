import matplotlib.pyplot as plt
from retinaface import RetinaFace
from PIL import Image
from deepface import DeepFace

import cv2
from ultralytics import YOLO
import math 


cap = cv2.VideoCapture('cctv_footage/CCTV2.mp4')
cap.set(3, 640)
cap.set(4, 480)
frameno = 0

while True:
    success, frame = cap.read()
    frameno+=1

    cv2.imwrite('cctvimg.jpg',frame)

    if frameno%5==0:
        try:
                
                obj = DeepFace.verify("cctvimg.jpg", "training_set/22BAI1468.jpeg"
                , model_name = 'ArcFace', detector_backend = 'retinaface')
                if obj['verified']:
                        print("Faiz detected")
                        fa= obj['facial_areas']['img1']
                        org = [fa['x'], fa['y']]
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        fontScale = 1
                        color = (255, 0, 0)
                        thickness = 2
                        cv2.rectangle(frame, (fa['x'], fa['y']), (fa['x']+fa['w'], (fa['y']+fa['h'])), (255, 0, 255), 3)
                        cv2.putText(frame, "faiz", org, font, fontScale, color, thickness)
                        cv2.imwrite("detections/faiz_spotted.jpg", frame)
                else:
                        print("not faiz")
                        obj2 = DeepFace.verify("cctvimg.jpg", "training_set/22BAI1313.jpg"
                , model_name = 'ArcFace', detector_backend = 'retinaface')
                        print("hmm")
                        if obj2['verified']:
                                print("Vamsee detected")
                                print(obj2)
                                fa= obj2['facial_areas']['img1']
                                org = [int(fa['x']), int(fa['y'])]
                                font = cv2.FONT_HERSHEY_SIMPLEX
                                fontScale = 1
                                color = (255, 0, 0)
                                thickness = 2
                                cv2.rectangle(frame, (int(fa['x']), int(fa['y'])), (int(fa['x']+fa['w']), int(fa['y']+fa['h'])), (255, 0, 255), 3)
                                cv2.putText(frame, "vamsee", org, font, fontScale, color, thickness)
                                cv2.imwrite("vamsee_spotted.jpg", frame)
                        else:
                               print("no vamsee")
                        
        except Exception as e:
                print(e)


        
    cv2.imshow('bruh', frame)
    if cv2.waitKey(1) == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()

"""
faces = RetinaFace.extract_faces()
print(faces)

for i, face in enumerate(faces):
   face =  Image.fromarray(face)
   face.save(f"face{i}.jpg")


obj = DeepFace.verify("faiz1.jpeg", "faiz2.jpeg"
          , model_name = 'ArcFace', detector_backend = 'opencv')
print(obj)
"""