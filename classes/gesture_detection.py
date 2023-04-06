from operator import ge
import cv2
import mediapipe as mp
import time
#from classes import gestures
#from classes.gesture import Gesture
import gestures
from gesture import Gesture

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

last_gesture = ""

while True:
    success, img = cap.read()

    width = img.shape[1]
    
    #width_cutoff = width // 2

    img1 = img[:, :width]

    imgRGB = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)Githu
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            landmarks = handLms.landmark
            for id, lm in enumerate(landmarks):
                #print(id, lm)
                h, w , c = img1.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                if id == 0:
                    cv2.circle(img1, (cx,cy), 4, (255,0,255), cv2.FILLED)
                
            mpDraw.draw_landmarks(img1, handLms, mpHands.HAND_CONNECTIONS)
       
        if gestures.is_schere(landmarks):
            print("Schere")
        if gestures.is_stein(landmarks):
            print("Stein")
        if gestures.is_papier(landmarks):
            print("Papier")
        if gestures.is_echse(landmarks):
            print("Echse")
        if gestures.is_spock(landmarks):
            print("Spock")
        
           
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img1, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    
    cv2.imshow("Hand-Tracking", img1)
    cv2.waitKey(1)
    