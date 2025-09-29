import cv2
import mediapipe as mp

mp_hand= mp.solutions.hands
mp_drawing= mp.solutions.drawing_utils

cap= cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence= 0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened:
        ret, frame= cap.read()
        if not ret:
            break
        
        frame= cv2.flip(frame, 1)
        rgb= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result= hands.process(rgb)
        
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)
                
                landmarks= hand_landmarks.landmark
                
                fingers= []
                
                if landmarks[4].x < landmarks[3].x:
                    fingers.append(1)
                else:
                    fingers.append(0)
                    
                    
                for tip in [8, 12, 16, 20]:
                    if landmarks[tip].y < landmarks[tip-2].y:
                        fingers.append(1)
                    else: 
                        fingers.append(0)
                
                count= sum(fingers)
            
                if count == 0:
                    text = "Rock"
                elif count == 2:
                    text = "Scissors"
                elif count == 5:
                    text = "Paper"
                else:
                    text = "Unknown"
                     
                cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
                
            cv2.imshow("Rock Paper Scissors", frame)
            
            if cv2.waitKey(1) & 0xFF == 27:
                break
            
cap.release()
cv2.destroyAllWindows()