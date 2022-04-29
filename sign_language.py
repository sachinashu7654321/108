import cv2
from cv2 import FILLED
from matplotlib.ft2font import LOAD_IGNORE_TRANSFORM
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips =[8, 12, 16, 20]
thumb_tip= 4

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        finger_fold_status=[]
        for hand_landmark in results.multi_hand_landmarks:
            #accessing the landmarks by their position
            lm_list=[]
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

             #Code goes here   
            for tips in finger_tips:
                x,y=int(lm_list[tips].x*w,int(lm_list[tips].y*h))
                cv2.circle(img,(x,y),15,(0,255,0),FILLED)

           

            if lm_list[tips].x > lm_list[tips-3].x:
                  cv2.circle(img,(x,y),15,(0,255,0),FILLED)
                  finger_fold_status.append(True)  
            else:
                finger_fold_status.append(False)

            mp_draw.draw_landmarks(img, hand_landmark,
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("hand tracking", img)
    cv2.waitKey(1)