import cv2
import mediapipe as mp
import time
import math


alpha_log = ['']*20
curr_alpha = ''

def main():
    global alpha_log, curr_alpha
    windowName = "Hand Tracker"
    cap = cv2.VideoCapture(0)
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    pTime = time.time()
    succ = True
    alpha_sim = False

    while succ:
        (succ, img) = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        output = hands.process(imgRGB)
        dist = []
        update_log = False
        curr_alpha = ''
        # print(alpha_log)

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
            i = 0
            for hand in lst:
                dist.append(calc_dist(hand))
                update_log = hand_rule(dist[i])
                i = i + 1
            i = 0

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        if not update_log:
            alpha_log.pop(0)
            alpha_log.append('')

        for i in range(0, len(alpha_log)-1):
            if curr_alpha == alpha_log[i] or curr_alpha == '':
                alpha_sim = True

        if not alpha_sim:
            print(curr_alpha)
        alpha_sim = False

        cv2.putText(img, "FPS: " + str(int(fps)), (10, 35), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
        cv2.imshow(windowName, img)
        pressedKey = cv2.waitKey(1) & 0xFF

        if pressedKey == 10 or pressedKey == 13 or pressedKey == 32:
            print("Print Hand Points")

            for hand in dist:
                for i in range(1, len(hand)-1):
                    print("Distance ", i, ": ", hand[i])
                print()
            print()

            """
            if output.multi_hand_landmarks:
                for handPoints in output.multi_hand_landmarks:
                    for id, lm in enumerate(handPoints.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x*w), int(lm.y*h)
                        #print("Point ", id, "\t: ", cx, "\t", cy)
                    print()
                print()
            print()
            """
        elif pressedKey == 27:
            succ = False
        elif cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1:
            succ = False

    cv2.destroyAllWindows()


def hand_rule(dist):
    global alpha_log, curr_alpha
    curr_alpha = ''
    # Error +15
    if (31 < dist[1] < 91 and 23 < dist[2] < 69 and 9 < dist[3] < 51 and 44 < dist[4] < 102 and
            0 < dist[5] < 43 and 16 < dist[6] < 60 and 0 < dist[7] < 21 and 4 < dist[8] < 40 and
            0 < dist[9] < 45 and 24 < dist[10] < 74 and 0 < dist[11] < 26 and 6 < dist[12] < 40 and
            0 < dist[13] < 39 and 18 < dist[14] < 68 and 0 < dist[15] < 23 and 15 < dist[16] < 47 and
            0 < dist[17] < 24 and 6 < dist[18] < 28 and 0 < dist[19] < 24 and 2 < dist[20] < 44 and
            34 < dist[21] < 86 and 0 < dist[22] < 36 and 1 < dist[23] < 47 and 6 < dist[24] < 44):
        curr_alpha = "A"

    alpha_log.pop(0)
    alpha_log.append(curr_alpha)

    return True


def calc_dist(hand):
    dist = [0] * 25
    # 0 is distance for ratio
    dist[0] = math.sqrt(math.pow((hand[0][0] - hand[9][0]), 2) + math.pow((hand[0][1] - hand[9][1]), 2))

    # 1-24 is distance for rule purpose
    dist[1] = math.sqrt(math.pow((hand[1][0] - hand[2][0]), 2) + math.pow((hand[1][1] - hand[2][1]), 2))
    dist[2] = math.sqrt(math.pow((hand[2][0] - hand[3][0]), 2) + math.pow((hand[2][1] - hand[3][1]), 2))
    dist[3] = math.sqrt(math.pow((hand[3][0] - hand[4][0]), 2) + math.pow((hand[3][1] - hand[4][1]), 2))
    dist[4] = math.sqrt(math.pow((hand[2][0] - hand[4][0]), 2) + math.pow((hand[2][1] - hand[4][1]), 2))
    dist[5] = math.sqrt(math.pow((hand[5][0] - hand[6][0]), 2) + math.pow((hand[5][1] - hand[6][1]), 2))
    dist[6] = math.sqrt(math.pow((hand[6][0] - hand[7][0]), 2) + math.pow((hand[6][1] - hand[7][1]), 2))
    dist[7] = math.sqrt(math.pow((hand[7][0] - hand[8][0]), 2) + math.pow((hand[7][1] - hand[8][1]), 2))
    dist[8] = math.sqrt(math.pow((hand[5][0] - hand[8][0]), 2) + math.pow((hand[5][1] - hand[8][1]), 2))
    dist[9] = math.sqrt(math.pow((hand[9][0] - hand[10][0]), 2) + math.pow((hand[9][1] - hand[10][1]), 2))
    dist[10] = math.sqrt(math.pow((hand[10][0] - hand[11][0]), 2) + math.pow((hand[10][1] - hand[11][1]), 2))
    dist[11] = math.sqrt(math.pow((hand[11][0] - hand[12][0]), 2) + math.pow((hand[11][1] - hand[12][1]), 2))
    dist[12] = math.sqrt(math.pow((hand[9][0] - hand[12][0]), 2) + math.pow((hand[9][1] - hand[12][1]), 2))
    dist[13] = math.sqrt(math.pow((hand[13][0] - hand[14][0]), 2) + math.pow((hand[13][1] - hand[14][1]), 2))
    dist[14] = math.sqrt(math.pow((hand[14][0] - hand[15][0]), 2) + math.pow((hand[14][1] - hand[15][1]), 2))
    dist[15] = math.sqrt(math.pow((hand[15][0] - hand[16][0]), 2) + math.pow((hand[15][1] - hand[16][1]), 2))
    dist[16] = math.sqrt(math.pow((hand[13][0] - hand[16][0]), 2) + math.pow((hand[13][1] - hand[16][1]), 2))
    dist[17] = math.sqrt(math.pow((hand[17][0] - hand[18][0]), 2) + math.pow((hand[17][1] - hand[18][1]), 2))
    dist[18] = math.sqrt(math.pow((hand[18][0] - hand[19][0]), 2) + math.pow((hand[18][1] - hand[19][1]), 2))
    dist[19] = math.sqrt(math.pow((hand[19][0] - hand[20][0]), 2) + math.pow((hand[19][1] - hand[20][1]), 2))
    dist[20] = math.sqrt(math.pow((hand[17][0] - hand[20][0]), 2) + math.pow((hand[17][1] - hand[20][1]), 2))
    dist[21] = math.sqrt(math.pow((hand[4][0] - hand[8][0]), 2) + math.pow((hand[4][1] - hand[8][1]), 2))
    dist[22] = math.sqrt(math.pow((hand[8][0] - hand[12][0]), 2) + math.pow((hand[8][1] - hand[12][1]), 2))
    dist[23] = math.sqrt(math.pow((hand[12][0] - hand[16][0]), 2) + math.pow((hand[12][1] - hand[16][1]), 2))
    dist[24] = math.sqrt(math.pow((hand[16][0] - hand[20][0]), 2) + math.pow((hand[16][1] - hand[20][1]), 2))

    dist[1] = dist[1] / dist[0] * 100
    dist[2] = dist[2] / dist[0] * 100
    dist[3] = dist[3] / dist[0] * 100
    dist[4] = dist[4] / dist[0] * 100
    dist[5] = dist[5] / dist[0] * 100
    dist[6] = dist[6] / dist[0] * 100
    dist[7] = dist[7] / dist[0] * 100
    dist[8] = dist[8] / dist[0] * 100
    dist[9] = dist[9] / dist[0] * 100
    dist[10] = dist[10] / dist[0] * 100
    dist[11] = dist[11] / dist[0] * 100
    dist[12] = dist[12] / dist[0] * 100
    dist[13] = dist[13] / dist[0] * 100
    dist[14] = dist[14] / dist[0] * 100
    dist[15] = dist[15] / dist[0] * 100
    dist[16] = dist[16] / dist[0] * 100
    dist[17] = dist[17] / dist[0] * 100
    dist[18] = dist[18] / dist[0] * 100
    dist[19] = dist[19] / dist[0] * 100
    dist[20] = dist[20] / dist[0] * 100
    dist[21] = dist[21] / dist[0] * 100
    dist[22] = dist[22] / dist[0] * 100
    dist[23] = dist[23] / dist[0] * 100
    dist[24] = dist[24] / dist[0] * 100

    return dist


if __name__ == "__main__":
    main()