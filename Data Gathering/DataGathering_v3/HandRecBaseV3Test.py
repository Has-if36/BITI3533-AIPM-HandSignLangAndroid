import cv2
import mediapipe as mp
import time
import math


alpha_log = ['']*5
curr_alpha = ''
sd = 15

datas = [
            # Letter 'A'
            [
                [100, 100], [55, 71], [42, 54], [27, 35], [66, 86], [11, 31], [31, 41], [4, 12], [15, 27], [11, 35],
                [42, 54], [5, 13], [15, 27], [9, 31], [36, 48], [5, 9], [15, 31], [6, 14], [22, 30], [2, 10],
                [12, 26], [45, 73], [16, 24], [19, 27], [18, 30], [24, 52], [42, 78], [66, 106], [87, 131], [34, 46],
                [25, 33], [44, 60], [64, 88], [47, 67], [32, 40], [30, 38], [49, 65], [62, 90], [52, 66], [28, 40],
                [33, 45], [82, 118], [69, 89], [44, 54], [20, 28]
            ]
        ]
alphas = ['A']


def main():
    global alpha_log, curr_alpha, datas
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
            if curr_alpha == alpha_log[i]:
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
    global i, alpha_log, curr_alpha, datas
    curr_alpha = ''
    for i, data in enumerate(datas):
    # Error +15
        if (data[1][0] - sd < dist[1] < data[1][1] + sd and data[2][0] - sd < dist[2] < data[2][1] + sd and
                data[3][0] - sd < dist[3] < data[3][1] + sd and data[4][0] - sd < dist[4] < data[4][1] + sd and
                data[5][0] - sd < dist[5] < data[5][1] + sd and data[6][0] - sd < dist[6] < data[6][1] + sd and
                data[7][0] - sd < dist[7] < data[7][1] + sd and data[8][0] - sd < dist[8] < data[8][1] + sd and
                data[9][0] - sd < dist[9] < data[9][1] + sd and data[10][0] - sd < dist[10] < data[10][1] + sd and
                data[11][0] - sd < dist[11] < data[11][1] + sd and data[12][0] - sd < dist[12] < data[12][1] + sd and
                data[13][0] - sd < dist[13] < data[13][1] + sd and data[14][0] - sd < dist[14] < data[14][1] + sd and
                data[15][0] - sd < dist[15] < data[15][1] + sd and data[16][0] - sd < dist[16] < data[16][1] + sd and
                data[17][0] - sd < dist[17] < data[17][1] + sd and data[18][0] - sd < dist[18] < data[18][1] + sd and
                data[19][0] - sd < dist[19] < data[19][1] + sd and data[20][0] - sd < dist[20] < data[20][1] + sd and
                data[21][0] - sd < dist[21] < data[21][1] + sd and data[22][0] - sd < dist[22] < data[22][1] + sd and
                data[23][0] - sd < dist[23] < data[23][1] + sd and data[24][0] - sd < dist[24] < data[24][1] + sd and

                data[25][0] - sd < dist[25] < data[25][1] + sd and data[26][0] - sd < dist[26] < data[26][1] + sd and
                data[27][0] - sd < dist[27] < data[27][1] + sd and data[28][0] - sd < dist[28] < data[28][1] + sd and
                data[29][0] - sd < dist[29] < data[29][1] + sd and data[30][0] - sd < dist[30] < data[30][1] + sd and
                data[31][0] - sd < dist[31] < data[31][1] + sd and data[32][0] - sd < dist[32] < data[32][1] + sd and
                data[33][0] - sd < dist[33] < data[33][1] + sd and data[20][0] - sd < dist[34] < data[34][1] + sd and
                data[35][0] - sd < dist[35] < data[35][1] + sd and data[22][0] - sd < dist[36] < data[36][1] + sd and
                data[37][0] - sd < dist[37] < data[37][1] + sd and data[24][0] - sd < dist[38] < data[38][1] + sd and
                data[39][0] - sd < dist[39] < data[39][1] + sd and data[40][0] - sd < dist[40] < data[40][1] + sd and
                data[41][0] - sd < dist[41] < data[41][1] + sd and data[42][0] - sd < dist[42] < data[42][1] + sd and
                data[43][0] - sd < dist[43] < data[43][1] + sd and data[44][0] - sd < dist[44] < data[44][1] + sd):
            curr_alpha = alphas[i]

    alpha_log.pop(0)
    alpha_log.append(curr_alpha)

    return True


def calc_dist(hand):
    global datas
    dist = [0] * len(datas[0])
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

    dist[25] = math.sqrt(math.pow((hand[4][0] - hand[5][0]), 2) + math.pow((hand[4][1] - hand[5][1]), 2))
    dist[26] = math.sqrt(math.pow((hand[4][0] - hand[9][0]), 2) + math.pow((hand[4][1] - hand[9][1]), 2))
    dist[27] = math.sqrt(math.pow((hand[4][0] - hand[13][0]), 2) + math.pow((hand[4][1] - hand[13][1]), 2))
    dist[28] = math.sqrt(math.pow((hand[4][0] - hand[17][0]), 2) + math.pow((hand[4][1] - hand[17][1]), 2))
    dist[29] = math.sqrt(math.pow((hand[8][0] - hand[2][0]), 2) + math.pow((hand[8][1] - hand[2][1]), 2))
    dist[30] = math.sqrt(math.pow((hand[8][0] - hand[9][0]), 2) + math.pow((hand[8][1] - hand[9][1]), 2))
    dist[31] = math.sqrt(math.pow((hand[8][0] - hand[13][0]), 2) + math.pow((hand[8][1] - hand[13][1]), 2))
    dist[32] = math.sqrt(math.pow((hand[8][0] - hand[17][0]), 2) + math.pow((hand[8][1] - hand[17][1]), 2))
    dist[33] = math.sqrt(math.pow((hand[12][0] - hand[2][0]), 2) + math.pow((hand[12][1] - hand[2][1]), 2))
    dist[34] = math.sqrt(math.pow((hand[12][0] - hand[5][0]), 2) + math.pow((hand[12][1] - hand[5][1]), 2))
    dist[35] = math.sqrt(math.pow((hand[12][0] - hand[13][0]), 2) + math.pow((hand[12][1] - hand[13][1]), 2))
    dist[36] = math.sqrt(math.pow((hand[12][0] - hand[17][0]), 2) + math.pow((hand[12][1] - hand[17][1]), 2))
    dist[37] = math.sqrt(math.pow((hand[16][0] - hand[2][0]), 2) + math.pow((hand[16][1] - hand[2][1]), 2))
    dist[38] = math.sqrt(math.pow((hand[16][0] - hand[5][0]), 2) + math.pow((hand[16][1] - hand[5][1]), 2))
    dist[39] = math.sqrt(math.pow((hand[16][0] - hand[9][0]), 2) + math.pow((hand[16][1] - hand[9][1]), 2))
    dist[40] = math.sqrt(math.pow((hand[16][0] - hand[17][0]), 2) + math.pow((hand[16][1] - hand[17][1]), 2))
    dist[41] = math.sqrt(math.pow((hand[20][0] - hand[2][0]), 2) + math.pow((hand[20][1] - hand[2][1]), 2))
    dist[42] = math.sqrt(math.pow((hand[20][0] - hand[5][0]), 2) + math.pow((hand[20][1] - hand[5][1]), 2))
    dist[43] = math.sqrt(math.pow((hand[20][0] - hand[9][0]), 2) + math.pow((hand[20][1] - hand[9][1]), 2))
    dist[44] = math.sqrt(math.pow((hand[20][0] - hand[13][0]), 2) + math.pow((hand[20][1] - hand[13][1]), 2))

    for i in range(1, len(datas[0])):
        dist[i] = dist[i] / dist[0] * 100

    return dist


if __name__ == "__main__":
    main()