package com.adastra.hasli;

public class HandSignData {
    // All alphabets except for 'J' and 'Z'
    private double[][][] dataAlpha = {
            // Letter 'A'
            {
                {100, 100}, {46, 76}, {38, 54}, {24, 36}, {59, 87}, {14, 28}, {31, 45},
                    {2, 6}, {19, 25}, {12, 30}, {39, 59}, {5, 11}, {21, 25}, {12, 24},
                    {33, 53}, {2, 8}, {20, 32}, {3, 9}, {21, 33}, {1, 9}, {17, 29},
                    {39, 71}, {15, 21}, {16, 32}, {21, 29}
            },
            // Letter 'I' & 'J'
            {
                {100, 100}, {22, 49}, {0, 43}, {0, 35}, {0, 71}, {27, 86}, {21, 41},
                    {13, 29}, {10, 106}, {29, 101}, {24, 48}, {-2, 21}, {5, 109}, {17, 97},
                    {18, 41}, {3, 26}, {20, 108}, {22, 72}, {15, 31}, {0, 32},
                    {32, 106}, // {87, 103}
                    {3, 53}, {16, 30}, {18, 46}, {32, 149}
                /*
                //Work but.. Too diverse
                {100, 100}, {22, 49}, {0, 43}, {0, 35}, {0, 71}, {27, 86}, {21, 41},
                    {13, 29}, {10, 106}, {29, 101}, {24, 48}, {-2, 21}, {5, 109}, {17, 97},
                    {18, 41}, {3, 26}, {20, 108}, {22, 72}, {15, 31}, {0, 32},
                    {32, 106}, // {87, 103}
                    {3, 53}, {16, 30}, {18, 46}, {32, 149}
                 */
                    /*
                    //Original
                    {100, 100}, {41, 49}, {35, 43}, {29, 35}, {61, 71}, {27, 31}, {21, 29},
                    {17, 21}, {10, 20}, {29, 33}, {36, 40}, {-2, 14}, {5, 13}, {17, 35},
                    {33, 41}, {14, 26}, {20, 46}, {33, 45}, {23, 31}, {24, 32},
                    {0, 103}, // {87, 103}
                    {33, 53}, {16, 30}, {18, 46}, {121, 149}
                     */
            },
            //Letter Z
            {
                {100, 100}, {22, 46}, {18, 36}, {25, 34}, {42, 67}, {8, 50}, {10, 31},
                    {12, 26}, {37, 105}, {6, 35}, {24, 39}, {2, 21}, {19, 72}, {6, 49},
                    {21, 38}, {2, 18}, {30, 82}, {8, 49}, {17, 31}, {1, 16}, {26, 79},
                    {62, 134}, {76, 135}, {15, 27}, {13, 21}
            }
    };

    // All alphabets
    //Temp
    private char[] listAlpha = {
            'A', 'I', 'Z'
    };

    /** Use this when complete
    private char[] listAlpha = {
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'y', 'Z'
    };
     */

    protected double[][][] getDataAlpha() {
        return dataAlpha;
    }

    protected  char[] getListAlpha() {
        return listAlpha;
    }
}