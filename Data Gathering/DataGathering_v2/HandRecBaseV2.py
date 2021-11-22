import cv2
import mediapipe as mp
import time
import math
import pandas as pd
import numpy as np
import os


def main():
    windowName = "Hand Tracker"
    cap = cv2.VideoCapture(0)
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1)
    mpDraw = mp.solutions.drawing_utils
    pTime = time.time()
    succ = True
    prevChar = ''
    currChar = ''
    printing = True
    title = ["Dist 0", "Dist 1", "Dist 2", "Dist 3", "Dist 4", "Dist 5", "Dist 6", "Dist 7", "Dist 8", "Dist 9",
             "Dist 10", "Dist 11", "Dist 12", "Dist 13", "Dist 14", "Dist 15", "Dist 16", "Dist 17", "Dist 18",
             "Dist 19", "Dist 20", "Dist 21", "Dist 22", "Dist 23", "Dist 24"]
    data = list()
    print("System will print ONCE when value reaches 95-105")
    print("Press 'Space' to reset & print another one")
    print("NOTE: Only possible for ONE hand")

    while succ:
        (succ, img) = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        output = hands.process(imgRGB)
        distance = 0
        dist = []

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
                dist.append(calc_dist(hand))

            distance = dist[0][0]

        if dist and printing:
            if 95 <= dist[0][0] <= 105:
                print("Distance Detected: ", dist[0][0], "\n")

                rule_dist = prep_rule(dist[0])
                for i, hand2_dist in enumerate(rule_dist):
                    print("\tRule Distance ", i, ": ", hand2_dist)
                print("\n")
                data.append(rule_dist)
                printing = False

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, "FPS: " + str(int(fps)), (10, 35), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
        cv2.imshow(windowName, img)
        pressedKey = cv2.waitKey(1) & 0xFF

        if pressedKey == 10 or pressedKey == 13:
            """
            print("Print Hand Points")
            if output.multi_hand_landmarks:
                #for handPoints in output.multi_hand_landmarks:
                #    for id, lm in enumerate(handPoints.landmark):
                #        h, w, c = img.shape
                #        cx, cy = int(lm.x*w), int(lm.y*h)
                #        print("Point ", id, "\t: ", cx, "\t", cy)
                #    print()
                for hand_dist in dist:
                    rule_dist = prep_rule(hand_dist)
                    #for i, hand2_dist in enumerate(hand_dist):
                    #    print("Actual Distance ", i, ": ", hand2_dist)
                    #print()
                    for i, hand2_dist in enumerate(rule_dist):
                        print("Rule Distance ", i, ": ", hand2_dist)
                print("Distance: ", distance)
            print("\n")
            """
        elif pressedKey == 32:
            print("Detect & Print again")
            printing = True
        elif pressedKey == 27 or cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1:
            if data:
                index = list(range(0, len(data[0])))
                print("Final Data")
                df = pd.DataFrame({'Distances': title}, index=index)

                for i in range(0, len(data)):
                    column = "Read " + str(i+1)
                    df[column] = data[i]

                if len(data) > 1:
                    avg = []
                    max = []
                    min = []
                    difference = []
                    max_round = []
                    min_round = []
                    avg_round = []
                    diff_round = []
                    index = []
                    for i in range(0, len(data[0])):
                        sum = 0
                        temp_max = 0
                        temp_min = 3999999999
                        for j in range(0, len(data)):
                            sum += data[j][i]
                            if data[j][i] > temp_max:
                                temp_max = data[j][i]
                            if data[j][i] < temp_min:
                                temp_min = data[j][i]
                        sum /= len(data)
                        avg.append(sum)
                        max.append(temp_max)
                        min.append(temp_min)
                        temp_max = round(temp_max)
                        temp_min = round(temp_min)
                        difference.append(temp_max-temp_min)
                        sum = round(sum)
                        avg_round.append(sum)
                        temp_diff=round((temp_max - temp_min) / 2)
                        diff_round.append(temp_diff)
                        min_round.append(sum - temp_diff)
                        max_round.append(sum + temp_diff)
                        index.append(i)

                    df['Read Avg'] = avg
                    df['Read Max'] = max
                    df['Read Min'] = min
                    df['Read Difference'] = difference
                    df['Round Avg'] = avg_round
                    df['+/-'] = diff_round
                    df['Round Min'] = min_round
                    df['Round Max'] = max_round
                    df['n'] = index

                print(df)
                i = 1
                filename = "read_" + str(i) + ".csv"

                if not os.path.exists(r"./HandRecBaseV2_output"):
                    os.mkdir(r"./HandRecBaseV2_output")

                while os.path.exists(os.path.join(r"./HandRecBaseV2_output", filename)):
                    i += 1
                    filename = "read_" + str(i) + ".csv"

                if not os.path.exists(os.path.join(r"./HandRecBaseV2_output", filename)):
                    path = os.path.join(r"./HandRecBaseV2_output", filename)
                    df.to_csv(path, index=False)

            succ = False

    cv2.destroyAllWindows()


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


def prep_rule(dist):
    dist_rule = [0] * 25

    # This is similar to, dist[1] / dist[0] * dist_rule[0] = dist_rule[1]
    # 0 is distance for ratio
    dist_rule[0] = 100
    ratio = dist_rule[0] / dist[0]

    # 1-24 is distance for rule purpose
    dist_rule[1] = ratio * dist[1]
    dist_rule[2] = ratio * dist[2]
    dist_rule[3] = ratio * dist[3]
    dist_rule[4] = ratio * dist[4]
    dist_rule[5] = ratio * dist[5]
    dist_rule[6] = ratio * dist[6]
    dist_rule[7] = ratio * dist[7]
    dist_rule[8] = ratio * dist[8]
    dist_rule[9] = ratio * dist[9]
    dist_rule[10] = ratio * dist[10]
    dist_rule[11] = ratio * dist[11]
    dist_rule[12] = ratio * dist[12]
    dist_rule[13] = ratio * dist[13]
    dist_rule[14] = ratio * dist[14]
    dist_rule[15] = ratio * dist[15]
    dist_rule[16] = ratio * dist[16]
    dist_rule[17] = ratio * dist[17]
    dist_rule[18] = ratio * dist[18]
    dist_rule[19] = ratio * dist[19]
    dist_rule[20] = ratio * dist[20]
    dist_rule[21] = ratio * dist[21]
    dist_rule[22] = ratio * dist[22]
    dist_rule[23] = ratio * dist[23]
    dist_rule[24] = ratio * dist[24]

    return dist_rule


if __name__ == "__main__":
    main()
