import cv2
import mediapipe as mp
import time
import math
import pandas as pd
import numpy as np
import os

dist_variance = 15
# For Every 2 Frames, for 30 frame (30 / 2 = 15)
title = [
            [
                "Dist 1-0", "Dist 1-1", "Dist 1-2", "Dist 1-3", "Dist 1-4", "Dist 1-5", "Dist 1-6", "Dist 1-7",
                "Dist 1-8", "Dist 1-9", "Dist 1-10", "Dist 1-11", "Dist 1-12", "Dist 1-13", "Dist 1-14", "Dist 1-15",
                "Dist 1-16", "Dist 1-17", "Dist 1-18", "Dist 1-19", "Dist 1-20", "Dist 1-21", "Dist 1-22", "Dist 1-23",
                "Dist 1-24"
            ],
            [
                "Dist 2-0", "Dist 2-1", "Dist 2-2", "Dist 2-3", "Dist 2-4", "Dist 2-5", "Dist 2-6", "Dist 2-7",
                "Dist 2-8", "Dist 2-9", "Dist 2-10", "Dist 2-11", "Dist 2-12", "Dist 2-13", "Dist 2-14", "Dist 2-15",
                "Dist 2-16", "Dist 2-17", "Dist 2-18", "Dist 2-19", "Dist 2-20", "Dist 2-21", "Dist 2-22", "Dist 2-23",
                "Dist 2-24"
            ],
            [
                "Dist 3-0", "Dist 3-1", "Dist 3-2", "Dist 3-3", "Dist 3-4", "Dist 3-5", "Dist 3-6", "Dist 3-7",
                "Dist 3-8", "Dist 3-9", "Dist 3-10", "Dist 3-11", "Dist 3-12", "Dist 3-13", "Dist 3-14", "Dist 3-15",
                "Dist 3-16", "Dist 3-17", "Dist 3-18", "Dist 3-19", "Dist 3-20", "Dist 3-21", "Dist 3-22", "Dist 3-23",
                "Dist 3-24"
            ],
            [
                "Dist 4-0", "Dist 4-1", "Dist 4-2", "Dist 4-3", "Dist 4-4", "Dist 4-5", "Dist 4-6", "Dist 4-7",
                "Dist 4-8", "Dist 4-9", "Dist 4-10", "Dist 4-11", "Dist 4-12", "Dist 4-13", "Dist 4-14", "Dist 4-15",
                "Dist 4-16", "Dist 4-17", "Dist 4-18", "Dist 4-19", "Dist 4-20", "Dist 4-21", "Dist 4-22", "Dist 4-23",
                "Dist 4-24"
            ],
            [
                "Dist 5-0", "Dist 5-1", "Dist 5-2", "Dist 5-3", "Dist 5-4", "Dist 5-5", "Dist 5-6", "Dist 5-7",
                "Dist 5-8", "Dist 5-9", "Dist 5-10", "Dist 5-11", "Dist 5-12", "Dist 5-13", "Dist 5-14", "Dist 5-15",
                "Dist 5-16", "Dist 5-17", "Dist 5-18", "Dist 5-19", "Dist 5-20", "Dist 5-21", "Dist 5-22", "Dist 5-23",
                "Dist 5-24"
            ],
            [
                "Dist 6-0", "Dist 6-1", "Dist 6-2", "Dist 6-3", "Dist 6-4", "Dist 6-5", "Dist 6-6", "Dist 6-7",
                "Dist 6-8", "Dist 6-9", "Dist 6-10", "Dist 6-11", "Dist 6-12", "Dist 6-13", "Dist 6-14", "Dist 6-15",
                "Dist 6-16", "Dist 6-17", "Dist 6-18", "Dist 6-19", "Dist 6-20", "Dist 6-21", "Dist 6-22", "Dist 6-23",
                "Dist 6-24"
            ]
        ]
letter = []
additional_item = 1  # which is Output
print(len(title) * len(title[0]))


def main():
    global title
    windowName = "Hand Tracker"
    cap = cv2.VideoCapture(0)
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1)
    mpDraw = mp.solutions.drawing_utils
    pTime = time.time()
    start_interval = pTime
    succ = True
    prevChar = ''
    currChar = ''
    # detection = False
    detection_count = len(title)
    read_num = 1

    data = list()
    temp_data = list()
    print("System will print ONCE when value reaches 95-105")
    print("Press 'Z' to test distance")
    print("Press 'Space' to scan")
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

        if dist and detection_count < len(title):
            interval = time.time() - start_interval
            if interval >= 0.25:
                print("Detection Index: ", detection_count, "\n")

                rule_dist = prep_rule(dist[0])
                for i, hand2_dist in enumerate(rule_dist):
                    print("\tRule Distance ", i, ": ", hand2_dist)
                    temp_data.append(hand2_dist)
                print("\n")

                start_interval = time.time()
                detection_count = detection_count + 1

                if detection_count == len(title):
                    character = ''
                    print("Reading Number ", read_num)
                    while True:
                        character = input("['A'-'Z'] | '/' to Cancel \nWhat letter is this? : ")
                        character = character.upper()
                        if 65 <= ord(character) <= 90:
                            read_num = read_num + 1
                            data.append(temp_data)
                            letter.append(character)
                            break
                        elif character == '/':
                            print("This data has been Cancelled")
                            break

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
        elif pressedKey == 90 or pressedKey == 122:
            try:
                if 100 - dist_variance <= dist[0][0] <= 100 + dist_variance:
                    print("Good spot")
                elif dist[0][0] < 100 - dist_variance:
                    print("Get your hand nearer to Camera")
                elif dist[0][0] > 100 + dist_variance:
                    print("Get your hand further from Camera")
            except:
                print("Hand not Detected")
        elif pressedKey == 32:
            print("Detecting for around 1.5 second & Printing")
            # detection = True
            detection_count = 0
            temp_data = list()
        elif pressedKey == 27 or cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1:
            reshape_title = []
            temp = []
            for i in range(0, len(title)):
                for j in range(0, len(title[i])):
                    reshape_title.append(title[i][j])
            reshape_title.append("Actual Output")

            if data:
                index = list(range(0, (len(data[0]) + additional_item)))
                print("Final Data")
                df = pd.DataFrame({'Distances': reshape_title}, index=index)

                for i in range(0, len(data)):
                    column = "Read " + str(i+1)
                    data[i].append(letter[i])
                    df[column] = data[i]

                """
                max_round = []
                min_round = []
                
                if len(data) > 1:
                    avg = []
                    max = []
                    min = []
                    difference = []
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
                        difference.append(temp_max - temp_min)
                        sum = round(sum)
                        avg_round.append(sum)
                        temp_diff = round((temp_max - temp_min) / 2)
                        diff_round.append(temp_diff)
                        min_round.append(sum - temp_diff)
                        max_round.append(sum + temp_diff)
                        index.append(i)
                else:
                    for i in range(0, len(data[0])):
                        min_round.append(round(data[0][i]))
                        max_round.append(round(data[0][i]))
                """

                df_T = df.set_index('Distances').T
                print(df_T)
                i = 1
                filename = "read_" + str(i)

                if not os.path.exists(r"./HandRecBaseV4_output"):
                    os.mkdir(r"./HandRecBaseV4_output")

                csv_file = filename + ".csv"
                while os.path.exists(os.path.join(r"./HandRecBaseV4_output", csv_file)):
                    i += 1
                    filename = "read_" + str(i)
                    csv_file = filename + ".csv"

                if not os.path.exists(os.path.join(r"./HandRecBaseV4_output", csv_file)):
                    path = os.path.join(r"./HandRecBaseV4_output", csv_file)
                    df_T.to_csv(path, index=True)

                text_file = filename + ".txt"
                if os.path.isfile(os.path.join(r'.\\HandRecBaseV4_output', text_file)):
                    f = open(os.path.join(r'.\\HandRecBaseV4_output', text_file), "w")
                else:
                    f = open(os.path.join(r'.\\HandRecBaseV4_output', text_file), "x")

                to_write_java = "// Java\n{\n\t"
                to_write_py = "# Python\n[\n\t"
                # print(min_round, max_round)
                """
                for j in range(0, len(title)):
                    # print(j)
                    if j == len(title) - 1:
                        to_write_java = to_write_java + "{" + str(min_round[j]) + ", " + str(max_round[j]) + "}\n}\n\n"
                        to_write_py = to_write_py + "[" + str(min_round[j]) + ", " + str(max_round[j]) + "]\n]\n"
                        # f.write("\t" + to_write_java + "\n")
                        break
                    else:
                        to_write_java = to_write_java + "{" + str(min_round[j]) + ", " + str(max_round[j]) + "}, "
                        to_write_py = to_write_py + "[" + str(min_round[j]) + ", " + str(max_round[j]) + "], "

                    if j % 10 == 9:
                        to_write_java = to_write_java + "\n\t"
                        to_write_py = to_write_py + "\n\t"
                        # f.write("\t" + to_write_java + "\n")
                """

                f.write(to_write_java)
                f.write(to_write_py)
                f.close()

            succ = False

    cv2.destroyAllWindows()


def calc_dist(hand):
    global title
    dist = [0] * len(title[0])
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

    """
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
    """

    for i in range(1, len(title[0])):
        dist[i] = dist[i] / dist[0] * 100

    """
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
    """

    return dist


def prep_rule(dist):
    global title
    dist_rule = [0] * len(title[0])

    # This is similar to, dist[1] / dist[0] * dist_rule[0] = dist_rule[1]
    # 0 is distance for ratio
    dist_rule[0] = 100
    ratio = dist_rule[0] / dist[0]

    # 1-24 is distance for rule purpose
    for i in range(1, len(title[0])):
        dist_rule[i] = ratio * dist[i]
    """
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
    """

    return dist_rule


if __name__ == "__main__":
    main()
