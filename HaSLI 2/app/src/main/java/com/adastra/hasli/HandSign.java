package com.adastra.hasli;

import android.app.Activity;
import android.content.Context;
import android.util.Log;
import android.view.Gravity;
import android.view.View;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.google.mediapipe.formats.proto.ClassificationProto;
import com.google.mediapipe.formats.proto.LandmarkProto;
import com.google.mediapipe.solutions.hands.HandLandmark;
import com.google.mediapipe.solutions.hands.Hands;
import com.google.mediapipe.solutions.hands.HandsOptions;
import com.google.mediapipe.solutions.hands.HandsResult;

import java.util.Locale;

public class HandSign {
    protected static String[] alphaLog = {
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
    };
    private static int fps = 30;
    private static int motionLogSize = 5;
    private static int alphaLogSize = 7 + motionLogSize;
    private String curr_alpha;
    private int sd = 10;
    private static double[] distBefore = new double[30];
    private static int[][] pointBefore = new int[30][2];
    //private static String latestMotion = "";
    private static int motionHoldDur = 30;
    private static int motionCurrDur = 0;
    private static int motionDurThresh = alphaLogSize * 2;
    private static int motionDur = 0;
    private static int confirm = 0;
    private final double ZDURMULTI = 2;
    Context context;

    protected void read(HandsResult result, Context context) {
        curr_alpha = "";
        int tempAlphaLogSize = alphaLogSize;
        alphaLogSize = fps/6 + motionLogSize;
        this.context = context;
        int hands = result.multiHandLandmarks().size();
        int[][] handPos = new int[21][2];
        //TextView textAlpha = (TextView) ((Activity)context).findViewById(R.id.text_alphabet);
        boolean alphaSim = false;

        // Cannot use 120, otherwise it will reach index 120
        if (alphaLogSize > 100) {alphaLogSize = 99;}

        if(alphaLogSize > tempAlphaLogSize) {
            int tempDiff = -(tempAlphaLogSize - alphaLogSize);
            for(int i = tempAlphaLogSize; i > 0; i--) {
                try {
                    alphaLog[i+tempDiff] = alphaLog[i];
                } catch (ArrayIndexOutOfBoundsException e) {
                    Log.e("Error", "ArrayIndexOutOfBoundsException", e);
                    alphaLogSize = 99;
                    break;
                }
            }
        } else if(alphaLogSize < tempAlphaLogSize) {
            int tempDiff = tempAlphaLogSize - alphaLogSize;
            for(int i = 0; i < tempAlphaLogSize; i++) {
                try {
                    alphaLog[i] = alphaLog[i+tempDiff];
                } catch (ArrayIndexOutOfBoundsException e) {
                    Log.e("Error", "ArrayIndexOutOfBoundsException", e);
                    alphaLogSize = 99;
                    break;
                }
            }
        }

        for(int i=0; i<hands; i++) {
            //Get Coordinate
            for (int j=0; j<21; j++) {
                LandmarkProto.NormalizedLandmark handLandmark = Hands.getHandLandmark(result, i, j);
                int width = result.inputBitmap().getWidth();
                int height = result.inputBitmap().getHeight();
                // 0=Pos X (Righter Pixel, Higher Value), 1=Pos Y (Lower Pixel, Higher Value)
                handPos[j][0] = Math.round(handLandmark.getX() * width);
                handPos[j][1] = Math.round(handLandmark.getY() * height);
                //Log.i("HandSign", String.format("Point %d: x=%d, y=%d", j, handPos[i][0], handPos[i][1]));
            }

            double[] dist = calculateDist(handPos);
            rule(dist, handPos);

            for (int j2 = 0; j2 < alphaLogSize; j2++) {
                if (j2 < alphaLogSize - 1) {
                    alphaLog[j2] = alphaLog[j2+1];
                    if (alphaLog[j2] == curr_alpha && j2 >= motionLogSize) {
                        alphaSim = true;
                    }
                } else {
                    alphaLog[j2] = curr_alpha;
                }
            }

            if (!alphaSim) {
                ((Activity) context).runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        // Need to adjust for J2 and so on later
                        if (!curr_alpha.equals("J2") && !curr_alpha.equals("J3") && !curr_alpha.equals("Z1") &&
                                !curr_alpha.equals("Z2") && !curr_alpha.equals("Z3") && !curr_alpha.equals("Z4")) {
                            TextView textAlpha = (TextView) ((Activity)context).findViewById(R.id.text_alphabet);
                            textAlpha.setText(curr_alpha);
                        } else if (curr_alpha.equals("Z1") || curr_alpha.equals("Z2") ||
                                curr_alpha.equals("Z3") || curr_alpha.equals("Z4")) {
                            TextView textAlpha = (TextView) ((Activity)context).findViewById(R.id.text_alphabet);
                            textAlpha.setText("Z?");
                        }
                    }
                });
            }

            //Log character
            //Log.i(TAG, String.format("Character ", ));
        }
    }

    protected void rule(double[] dist, int[][] handPos) {
        HandSignData hsd = new HandSignData();
        double[][][] dataAlpha = hsd.getDataAlpha();
        char[] listAlpha = hsd.getListAlpha();
        //String latestMotion = "";
        boolean motion = false;
        //int motionDurThresh = alphaLogSize * 3 / 4, motionDur = 0;

        if (motionCurrDur == 0) {
            if (!alphaLog[alphaLogSize-1].equals("J2") && !alphaLog[alphaLogSize-1].equals("J3") &&
                    !alphaLog[alphaLogSize-1].equals("Z2") && !alphaLog[alphaLogSize-1].equals("Z3") &&
                    !alphaLog[alphaLogSize-1].equals("Z4")) {
                for (int i = 0; i < dataAlpha.length; i++) {
                    if (dist[1] > dataAlpha[i][1][0] - sd && dist[1] < dataAlpha[i][1][1] + sd &&
                            dist[2] > dataAlpha[i][2][0] - sd && dist[2] < dataAlpha[i][2][1] + sd &&
                            dist[3] > dataAlpha[i][3][0] - sd && dist[3] < dataAlpha[i][3][1] + sd &&
                            dist[4] > dataAlpha[i][4][0] - sd && dist[4] < dataAlpha[i][4][1] + sd &&
                            dist[5] > dataAlpha[i][5][0] - sd && dist[5] < dataAlpha[i][5][1] + sd &&
                            dist[6] > dataAlpha[i][6][0] - sd && dist[6] < dataAlpha[i][6][1] + sd &&
                            dist[7] > dataAlpha[i][7][0] - sd && dist[7] < dataAlpha[i][7][1] + sd &&
                            dist[8] > dataAlpha[i][8][0] - sd && dist[8] < dataAlpha[i][8][1] + sd &&
                            dist[9] > dataAlpha[i][9][0] - sd && dist[9] < dataAlpha[i][9][1] + sd &&
                            dist[10] > dataAlpha[i][10][0] - sd && dist[10] < dataAlpha[i][10][1] + sd &&
                            dist[11] > dataAlpha[i][11][0] - sd && dist[11] < dataAlpha[i][11][1] + sd &&
                            dist[12] > dataAlpha[i][12][0] - sd && dist[12] < dataAlpha[i][12][1] + sd &&
                            dist[13] > dataAlpha[i][13][0] - sd && dist[13] < dataAlpha[i][13][1] + sd &&
                            dist[14] > dataAlpha[i][14][0] - sd && dist[14] < dataAlpha[i][14][1] + sd &&
                            dist[15] > dataAlpha[i][15][0] - sd && dist[15] < dataAlpha[i][15][1] + sd &&
                            dist[16] > dataAlpha[i][16][0] - sd && dist[16] < dataAlpha[i][16][1] + sd &&
                            dist[17] > dataAlpha[i][17][0] - sd && dist[17] < dataAlpha[i][17][1] + sd &&
                            dist[18] > dataAlpha[i][18][0] - sd && dist[18] < dataAlpha[i][18][1] + sd &&
                            dist[19] > dataAlpha[i][19][0] - sd && dist[19] < dataAlpha[i][19][1] + sd &&
                            dist[20] > dataAlpha[i][20][0] - sd && dist[20] < dataAlpha[i][20][1] + sd &&
                            dist[21] > dataAlpha[i][21][0] - sd && dist[21] < dataAlpha[i][21][1] + sd &&
                            dist[22] > dataAlpha[i][22][0] - sd && dist[22] < dataAlpha[i][22][1] + sd &&
                            dist[23] > dataAlpha[i][23][0] - sd && dist[23] < dataAlpha[i][23][1] + sd &&
                            dist[24] > dataAlpha[i][24][0] - sd && dist[24] < dataAlpha[i][24][1] + sd) {
                        curr_alpha = Character.toString(listAlpha[i]);
                        if(curr_alpha.equals("Z")) {curr_alpha = "Z1";}
                        if ((curr_alpha.equals("I") || curr_alpha.equals("Z1")) && distBefore.length == 30) {
                            distBefore = dist;
                            pointBefore = handPos;
                        }
                    }
                }
            } else {
                if (alphaLog[alphaLogSize-1].equals("J2") || alphaLog[alphaLogSize-1].equals("J3") ||
                        alphaLog[alphaLogSize-1].equals("Z2") ||
                        alphaLog[alphaLogSize-1].equals("Z3") || alphaLog[alphaLogSize-1].equals("Z4")) {
                    motion = true;
                }

                boolean incMotionDur = false;
                for (int j = alphaLogSize; j > 0; j--) {
                    if (alphaLog[j].equals("J2") || alphaLog[j].equals("J3") ||
                            alphaLog[j].equals("Z2") ||
                            alphaLog[j].equals("Z3") || alphaLog[j].equals("Z4")) {
                        motion = true;
                        //latestMotion = alphaLog[j];
                        if(curr_alpha.equals(""))
                            curr_alpha = alphaLog[j];
                        else {
                            incMotionDur = true;
                            if (motionDur > motionDurThresh * ZDURMULTI && (alphaLog[j].equals("Z2") ||
                                    alphaLog[j].equals("Z3") || alphaLog[j].equals("Z4"))) {
                                curr_alpha = "";
                                motion = false;
                                break;
                            } else if (motionDur > motionDurThresh && !(alphaLog[j].equals("Z2") ||
                                    alphaLog[j].equals("Z3") || alphaLog[j].equals("Z4"))) {
                                curr_alpha = "";
                                motion = false;
                                break;
                            }
                        }
                    }
                }
                if (incMotionDur) motionDur++;
            }

            /*
            if (curr_alpha.equals("")) {
                if (alphaLog[alphaLogSize-1].equals("J2") || alphaLog[alphaLogSize-1].equals("J3") ||
                        alphaLog[alphaLogSize-1].equals("Z1") || alphaLog[alphaLogSize-1].equals("Z2") ||
                        alphaLog[alphaLogSize-1].equals("Z3") || alphaLog[alphaLogSize-1].equals("Z4")) {
                    motion = true;
                }

                //Below Here got Comment
                for (int j = alphaLogSize; j > 0; j--) {
                    if (alphaLog[j].equals("J2") || alphaLog[j].equals("J3") ||
                            alphaLog[j].equals("Z1") || alphaLog[j].equals("Z2") ||
                            alphaLog[j].equals("Z3") || alphaLog[j].equals("Z4")) {
                        motion = true;
                        //latestMotion = alphaLog[j];
                        if(curr_alpha.equals(""))
                            curr_alpha = alphaLog[j];
                        else {
                            motionDur++;
                            if (motionDur > motionDurThresh) {
                                curr_alpha = "";
                                motion = false;
                                break;
                            }
                        }
                    }
                }
            }
            */

            if (!motion) {
                //dist[20] < distBefore[20]
                if (curr_alpha.equals("I") && (handPos[18][1] > handPos[9][1] || dist[20] < distBefore[20] - sd * 2)) {
                    //latestMotion = "J2";
                    curr_alpha = "J2";
                    distBefore = dist;
                }
                else if (curr_alpha.equals("Z1") && handPos[8][0] > pointBefore[8][0] &&
                        handPos[8][1] > pointBefore[8][1] - distBefore[0] / 7 &&
                        handPos[8][1] < pointBefore[8][1] + distBefore[0] / 7) {
                    curr_alpha = "Z2";
                    distBefore = dist;
                    pointBefore = handPos;
                }
                else if (curr_alpha.equals("I") || curr_alpha.equals("Z1")) {
                    //Pass
                } else {
                    //latestMotion = "";
                    motionDur = 0;
                    distBefore = new double[30]; //Dummily set to 30
                    pointBefore = new int[30][2];
                }
            } else {
                //dist[20] < distBefore[20] - sd / 4 &&
                if ((curr_alpha.equals("J2") || curr_alpha.equals("J3")) && dist[20] < distBefore[20] + sd * 2 / 2.0 && //handPos[18][1] > handPos[9][1] &&
                        dist[16] < distBefore[16] + sd * 8 &&
                        dist[12] < distBefore[12] + sd * 8 && dist[8] < distBefore[8] + sd * 8
                ) {
                    // latestMotion = "J3";
                    if (curr_alpha.equals("J2")) {
                        distBefore = dist;
                    }
                    curr_alpha = "J3";
                }

                if (curr_alpha.equals("J3") && dist[20] > distBefore[20] - sd * 2 &&
                        dist[16] < distBefore[16] + sd * 8 &&
                        dist[12] < distBefore[12] + sd * 8 && dist[8] < distBefore[8] + sd * 8) {
                    curr_alpha = "J";
                    motionCurrDur = 1;
                    //latestMotion = "";
                    distBefore = new double[30];
                    pointBefore = new int[30][2];
                }

                if ((curr_alpha.equals("Z2") || curr_alpha.equals("Z3")) && handPos[8][0] > pointBefore[8][0] + sd &&
                        handPos[8][1] > pointBefore[8][1] - distBefore[0] / 7 &&
                        handPos[8][1] < pointBefore[8][1] + distBefore[0] / 7 &&
                        dist[16] < distBefore[16] + sd &&
                        dist[12] < distBefore[12] + sd && dist[8] < distBefore[8] + sd) {
                    curr_alpha = "Z3";
                    distBefore = dist;
                    pointBefore = handPos;
                }

                if ((curr_alpha.equals("Z3") || curr_alpha.equals("Z4")) &&
                        handPos[8][0] < pointBefore[8][0] - sd && handPos[8][1] > pointBefore[8][1] + sd &&
                        dist[16] < distBefore[16] + sd && dist[12] < distBefore[12] + sd &&
                        dist[8] < distBefore[8] + sd
                ) {
                    curr_alpha = "Z4";
                    distBefore = dist;
                    pointBefore = handPos;
                }

                if (curr_alpha.equals("Z4") && handPos[8][0] > pointBefore[8][0] &&
                        handPos[8][1] > pointBefore[8][1] - distBefore[0] / 7 &&
                        handPos[8][1] < pointBefore[8][1] + distBefore[0] / 7 &&
                        dist[16] < distBefore[16] + sd &&
                        dist[12] < distBefore[12] + sd && dist[8] < distBefore[8] + sd ) {
                    curr_alpha = "Z";
                    motionCurrDur = 1;
                    //latestMotion = "";
                    distBefore = new double[30];
                    pointBefore = new int[30][2];
                }
            }
        } else {
            boolean containJZ = false;
            for (int i = 0;  i < alphaLogSize; i++) {
                if (alphaLog[i].equals("J") || alphaLog[i].equals("Z")) {
                    curr_alpha = alphaLog[i];
                    containJZ = true;
                }
            }
            if (!containJZ) {
                curr_alpha = "";
                motionCurrDur = 0;
            }
            else if (containJZ && motionCurrDur < motionHoldDur) {
                motionCurrDur++;
            } else {
                curr_alpha = "";
            }
        }

        String test = "";
        for (int j2 = 0; j2 < alphaLogSize; j2++) {
            test = test + alphaLog[j2] + ", ";
        }
        Log.i("HandSign", String.format("{%s}", test));
        Log.i("HandSign", String.format("posCurr: %d, posBef: %d", handPos[8][0], pointBefore[8][0]));
        Log.i("HandSign", "Motion: " + motion);
        Log.i("HandSign", "MotionDur: " + motionDur + "MotionThresh: " + motionDurThresh * ZDURMULTI);

        //Log.i("HandSign", String.format("Reading %s", curr_alpha));
        //Log.i("HandSign", String.format("Reading 2 %s", latestMotion));
        /*
        Log.i("HandSign", String.format("Point 18: %d, Point 9: %d", handPos[18][1], handPos[9][1]));
        if (handPos[18][1] > handPos[9][1]) {
            Log.i("HandSign", "18 HIGHER 9");
        }
         */
    }

    protected double[] calculateDist(int[][] handPos) {
        double[] dist = new double[25];

        // 0 is distance for ratio
        dist[0] = Math.sqrt(Math.pow((handPos[0][0] - handPos[9][0]), 2) + Math.pow((handPos[0][1] - handPos[9][1]), 2));

        // 1-24 is distance for rule purpose
        dist[1] = Math.sqrt(Math.pow((handPos[1][0] - handPos[2][0]), 2) + Math.pow((handPos[1][1] - handPos[2][1]), 2));
        dist[2] = Math.sqrt(Math.pow((handPos[2][0] - handPos[3][0]), 2) + Math.pow((handPos[2][1] - handPos[3][1]), 2));
        dist[3] = Math.sqrt(Math.pow((handPos[3][0] - handPos[4][0]), 2) + Math.pow((handPos[3][1] - handPos[4][1]), 2));
        dist[4] = Math.sqrt(Math.pow((handPos[2][0] - handPos[4][0]), 2) + Math.pow((handPos[2][1] - handPos[4][1]), 2));
        dist[5] = Math.sqrt(Math.pow((handPos[5][0] - handPos[6][0]), 2) + Math.pow((handPos[5][1] - handPos[6][1]), 2));
        dist[6] = Math.sqrt(Math.pow((handPos[6][0] - handPos[7][0]), 2) + Math.pow((handPos[6][1] - handPos[7][1]), 2));
        dist[7] = Math.sqrt(Math.pow((handPos[7][0] - handPos[8][0]), 2) + Math.pow((handPos[7][1] - handPos[8][1]), 2));
        dist[8] = Math.sqrt(Math.pow((handPos[5][0] - handPos[8][0]), 2) + Math.pow((handPos[5][1] - handPos[8][1]), 2));
        dist[9] = Math.sqrt(Math.pow((handPos[9][0] - handPos[10][0]), 2) + Math.pow((handPos[9][1] - handPos[10][1]), 2));
        dist[10] = Math.sqrt(Math.pow((handPos[10][0] - handPos[11][0]), 2) + Math.pow((handPos[10][1] - handPos[11][1]), 2));
        dist[11] = Math.sqrt(Math.pow((handPos[11][0] - handPos[12][0]), 2) + Math.pow((handPos[11][1] - handPos[12][1]), 2));
        dist[12] = Math.sqrt(Math.pow((handPos[9][0] - handPos[12][0]), 2) + Math.pow((handPos[9][1] - handPos[12][1]), 2));
        dist[13] = Math.sqrt(Math.pow((handPos[13][0] - handPos[14][0]), 2) + Math.pow((handPos[13][1] - handPos[14][1]), 2));
        dist[14] = Math.sqrt(Math.pow((handPos[14][0] - handPos[15][0]), 2) + Math.pow((handPos[14][1] - handPos[15][1]), 2));
        dist[15] = Math.sqrt(Math.pow((handPos[15][0] - handPos[16][0]), 2) + Math.pow((handPos[15][1] - handPos[16][1]), 2));
        dist[16] = Math.sqrt(Math.pow((handPos[13][0] - handPos[16][0]), 2) + Math.pow((handPos[13][1] - handPos[16][1]), 2));
        dist[17] = Math.sqrt(Math.pow((handPos[17][0] - handPos[18][0]), 2) + Math.pow((handPos[17][1] - handPos[18][1]), 2));
        dist[18] = Math.sqrt(Math.pow((handPos[18][0] - handPos[19][0]), 2) + Math.pow((handPos[18][1] - handPos[19][1]), 2));
        dist[19] = Math.sqrt(Math.pow((handPos[19][0] - handPos[20][0]), 2) + Math.pow((handPos[19][1] - handPos[20][1]), 2));
        dist[20] = Math.sqrt(Math.pow((handPos[17][0] - handPos[20][0]), 2) + Math.pow((handPos[17][1] - handPos[20][1]), 2));
        dist[21] = Math.sqrt(Math.pow((handPos[4][0] - handPos[8][0]), 2) + Math.pow((handPos[4][1] - handPos[8][1]), 2));
        dist[22] = Math.sqrt(Math.pow((handPos[8][0] - handPos[12][0]), 2) + Math.pow((handPos[8][1] - handPos[12][1]), 2));
        dist[23] = Math.sqrt(Math.pow((handPos[12][0] - handPos[16][0]), 2) + Math.pow((handPos[12][1] - handPos[16][1]), 2));
        dist[24] = Math.sqrt(Math.pow((handPos[16][0] - handPos[20][0]), 2) + Math.pow((handPos[16][1] - handPos[20][1]), 2));

        dist[1] = dist[1] / dist[0] * 100;
        dist[2] = dist[2] / dist[0] * 100;
        dist[3] = dist[3] / dist[0] * 100;
        dist[4] = dist[4] / dist[0] * 100;
        dist[5] = dist[5] / dist[0] * 100;
        dist[6] = dist[6] / dist[0] * 100;
        dist[7] = dist[7] / dist[0] * 100;
        dist[8] = dist[8] / dist[0] * 100;
        dist[9] = dist[9] / dist[0] * 100;
        dist[10] = dist[10] / dist[0] * 100;
        dist[11] = dist[11] / dist[0] * 100;
        dist[12] = dist[12] / dist[0] * 100;
        dist[13] = dist[13] / dist[0] * 100;
        dist[14] = dist[14] / dist[0] * 100;
        dist[15] = dist[15] / dist[0] * 100;
        dist[16] = dist[16] / dist[0] * 100;
        dist[17] = dist[17] / dist[0] * 100;
        dist[18] = dist[18] / dist[0] * 100;
        dist[19] = dist[19] / dist[0] * 100;
        dist[20] = dist[20] / dist[0] * 100;
        dist[21] = dist[21] / dist[0] * 100;
        dist[22] = dist[22] / dist[0] * 100;
        dist[23] = dist[23] / dist[0] * 100;
        dist[24] = dist[24] / dist[0] * 100;
        return dist;
    }

    protected int getAlphaLogSize() {
        return alphaLogSize;
    }

    protected void setFPS(int fps) {
        if (fps > 60) {
            this.fps = 60;
        } else {
            this.fps = fps;
        }
    }
}
