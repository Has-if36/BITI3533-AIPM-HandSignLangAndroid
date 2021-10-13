import cv2
import mediapipe as mp
import time


def main():
    windowName = "Hand Tracker"
    cap = cv2.VideoCapture(0)
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    pTime = time.time()
    succ = True
    prevChar = ''
    currChar = ''

    while succ:
        (succ, img) = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        output = hands.process(imgRGB)

        if output.multi_hand_landmarks:
            lst = []
            lst_2 = []
            for handPoints in output.multi_hand_landmarks:
                lst_2.clear()
                mpDraw.draw_landmarks(img, handPoints, mpHands.HAND_CONNECTIONS)
                for id, lm in enumerate(handPoints.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lst_2.append((cx, cy))
                lst.append(lst_2)

            # Hand Sign Start Here
            for hand in lst:
                if (hand[4][0] > hand[6][0] and hand[3][1] > hand[4][1] and hand[7][1] > hand[6][1]
and hand[7][1] > hand[6][1] and hand[11][1] > hand[10][1] and hand[15][1] > hand[14][1] and hand[19][1] > hand[18][1]\
and hand[0][1] > hand[2][1] and hand[1][1] > hand[2][1] and hand[0][0] < hand[2][0] and hand[1][0] < hand[2][0]\
and hand[4][0] < hand[3][0] and hand[2][1] > hand[11][1]):
                    currChar = 'A'
                elif (hand[4][0] > hand[6][0]):
                    # Cotinue...
                    currChar = ""
                elif (hand[4][0] > hand[6][0]):
                    # Cotinue...
                    currChar = ""
                elif (hand[4][0] > hand[6][0]):
                    # Cotinue...
                    currChar = ""
                else:
                    currChar = ""

            if prevChar != currChar:
                prevChar = currChar
                if currChar != '':
                    print(currChar, "\t", pTime)


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, "FPS: " + str(int(fps)), (10, 35), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
        cv2.imshow(windowName, img)
        pressedKey = cv2.waitKey(1) & 0xFF

        if pressedKey == 10 or pressedKey == 13 or pressedKey == 32:
            print("Print Hand Points")
            if output.multi_hand_landmarks:
                for handPoints in output.multi_hand_landmarks:
                    for id, lm in enumerate(handPoints.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x*w), int(lm.y*h)
                        print("Point ", id, "\t: ", cx, "\t", cy)
                    print()
                print()
            print()
        elif pressedKey == 27:
            succ = False
        elif cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1:
            succ = False

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()