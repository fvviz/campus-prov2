
from retinaface import RetinaFace
from PIL import Image
from deepface import DeepFace
import cv2
import os


def scan_for_user(img_file_name, footage):
        filename=os.path.basename(footage)
        cap = cv2.VideoCapture(footage)
        cap.set(3, 640)
        cap.set(4, 480)
        frameno = 0
        count = 0

        while True:
                success, frame = cap.read()
                frameno+=1
                
                cv2.imwrite('cctvimg.jpg',frame)
                if frameno%5==0:
                                print("frame check, count_check=", count)
                                try:
                                        print("checking, count=", count)
                                        obj = DeepFace.verify("cctvimg.jpg", img_file_name, model_name = 'ArcFace', detector_backend = 'retinaface')
                                        if obj['verified']:
                                                print("found the nigga")
                                                count +=1
                                                print("incremented count=", count)
                                                fa= obj['facial_areas']['img1']
                                                org = [fa['x'], fa['y']]
                                                font = cv2.FONT_HERSHEY_SIMPLEX
                                                fontScale = 1
                                                color = (255, 0, 0)
                                                thickness = 2
                                                name = os.path.basename(img_file_name).split(".")[0]
                                                cv2.putText(frame, name, org, font, fontScale, color, thickness)
                                                cv2.imwrite(f"detections/{name}.jpg", frame)
                                                print("wrote him in ")
                                        
                                        if count==3:
                                                print("count is 3")
                                                name = img_file_name.split(".")[0]
                                                return filename
                                                #return f"User Last seen by {filename} in MG auditorium"
                                                
                                except Exception as e:
                                        print("no face burh")
                                    
        cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    print(os.path.isfile("cctv_footage/CCTV2.mp4"))
    scan_for_user("training_set/22BAI1313.jpg", "cctv_footage/CCTV2.mp4")