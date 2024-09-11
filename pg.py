import cv2
import mediapipe as mp
import pyautogui
pyautogui.FAILSAFE = False
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
screen_width , screen_height = pyautogui.size()
#cv2.namedWindow('MediaPipe Hands', cv2.WINDOW_NORMAL)

# Set the window to fullscreen
#cv2.setWindowProperty('MediaPipe Hands', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
def pressi(hand_landmarks):
    thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
    index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

    thumb_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
    index_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
    middle_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
    ring_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
    pinky_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y

    if (thumb_tip_y < thumb_mcp_y and 
        index_tip_y < index_mcp_y and
        middle_tip_y < middle_mcp_y and ring_tip_y > ring_mcp_y and pinky_tip_y > pinky_mcp_y ):
        return True
    return False
def backspace(hand_landmarks):
    thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
    idex_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip_y = hand_landmar.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip_yndmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

    thumb_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
    index_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    middle_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    ring_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
    pinky_pip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y

    thumb_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
    index_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
    middle_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
    ring_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
    pinky_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y

    #thumb_dip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_DIP].y
    index_dip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
    middle_dip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
    ring_dip_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y
    pinky_dip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y


    if ((thumb_tip_y > thumb_pip_y and 
        index_tip_y > index_pip_y and
        middle_tip_y > middle_pip_y and
        ring_tip_y > ring_pip_y and
        pinky_tip_y > pinky_pip_y)) or (thumb_mcp_y < thumb_pip_y and 
        index_mcp_y < index_pip_y and
        middle_mcp_y < middle_pip_y and
        ring_mcp_y < ring_pip_y and
        pinky_mcp_y < pinky_pip_y) or (  
        index_mcp_y < index_dip_y and
        middle_mcp_y < middle_dip_y and
        ring_mcp_y < ring_dip_y and
        pinky_mcp_y < pinky_dip_y):
        return True
    return False
def click(hand_landmarks):
    thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
    index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

    thumb_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
    index_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
    middle_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
    ring_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
    pinky_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y

    if (thumb_tip_y < thumb_mcp_y and 
        index_tip_y < index_mcp_y and
        middle_tip_y < middle_mcp_y and
        ring_tip_y < ring_mcp_y and
        pinky_tip_y < pinky_mcp_y):
        return True
    return False
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  click_flag = False
  backspace_flag = False
  i_flag = False
  while cap.isOpened():
    success, image = cap.read()
    
 
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    
     
    results = hands.process(image)
    image_height , image_width , _ = image.shape


    
     
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        for ids, landmark in enumerate(hand_landmarks.landmark):
          cx , cy =  int(landmark.x * image_width) , int(landmark.y*image_height)
          if (ids==8):
           
         
           pyautogui.moveTo(cx+700,cy+300)
             
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        if click(hand_landmarks):
          pyautogui.click()
          click_flag = True
        if backspace(hand_landmarks):
          pyautogui.press('backspace')
          backspace_flag = True
        if pressi(hand_landmarks):
          pyautogui.press('i')
          i_flag = True
    cv2.imshow('Mouse',image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()   