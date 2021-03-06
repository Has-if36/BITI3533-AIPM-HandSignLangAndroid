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
            // Letter 'B'
            {
                    {100, 100}, {36, 42}, {27, 35}, {17, 27}, {36, 58}, {31, 39}, {17, 25},
                    {15, 21}, {62, 82}, {38, 42}, {22, 26}, {16, 24}, {76, 92}, {36, 40},
                    {19, 27}, {16, 22}, {71, 87}, {28, 32}, {17, 21}, {15, 19}, {61, 69},
                    {59, 95}, {19, 35}, {11, 23}, {14, 38}
            },
            // Letter 'C'
            {
                    {100, 100}, {31, 43}, {26, 30}, {21, 27}, {46, 56}, {28, 40}, {14, 32},
                    {9, 25}, {36, 88}, {40, 48}, {20, 36}, {17, 27}, {40, 96}, {39, 51},
                    {24, 36}, {19, 27}, {44, 100}, {31, 43}, {21, 29}, {17, 21}, {52, 84},
                    {32, 58}, {0, 12}, {-1, 11}, {2, 18}
            },
            // Letter 'D'
            {
                    {100, 100}, {37, 45}, {25, 37}, {18, 30}, {40, 62}, {36, 46}, {21, 29},
                    {20, 24}, {78, 96}, {23, 35}, {19, 43}, {7, 27}, {17, 43}, {17, 29},
                    {28, 36}, {9, 19}, {27, 51}, {16, 28}, {20, 28}, {6, 14}, {26, 44},
                    {72, 96}, {91, 131}, {10, 46}, {13, 21}
            },
            // Letter 'E'
            {
                    {100, 100}, {44, 50}, {30, 38}, {24, 32}, {43, 59}, {33, 45}, {14, 34},
                    {16, 24}, {3, 19}, {30, 54}, {22, 38}, {13, 27}, {0, 20}, {26, 52},
                    {22, 34}, {12, 26}, {7, 21}, {19, 41}, {16, 24}, {10, 22}, {13, 23},
                    {30, 38}, {18, 26}, {15, 23}, {16, 20}
            },
            // Letter 'F'
            {
                    {100, 100}, {38, 46}, {30, 38}, {21, 33}, {44, 64}, {29, 35}, {1, 17},
                    {9, 17}, {-13, 51}, {36, 50}, {22, 30}, {19, 27}, {78, 106}, {35, 47},
                    {22, 30}, {16, 28}, {71, 105}, {30, 36}, {18, 24}, {15, 23}, {63, 83},
                    {-23, 49}, {37, 127}, {18, 28}, {21, 41}
            },
            // Letter 'G'
            {
                    {100, 100}, {27, 47}, {19, 39}, {10, 34}, {26, 70}, {26, 56}, {9, 41},
                    {12, 30}, {38, 126}, {15, 53}, {0, 36}, {2, 26}, {3, 67}, {2, 56},
                    {2, 32}, {3, 23}, {6, 66}, {1, 47}, {-1, 27}, {3, 17}, {11, 53},
                    {33, 129}, {25, 165}, {20, 28}, {14, 28}
            },
            // Letter 'H'
            {
                    {100, 100}, {39, 45}, {29, 41}, {24, 34}, {42, 70}, {27, 33}, {23, 33},
                    {15, 23}, {10, 30}, {20, 30}, {28, 40}, {9, 25}, {10, 44}, {17, 37},
                    {29, 37}, {19, 27}, {20, 44}, {32, 40}, {15, 31}, {17, 31}, {64, 100},
                    {12, 48}, {15, 29}, {8, 32}, {97, 145}
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
            // Letter 'K'
            {
                    {100, 100}, {41, 53}, {28, 40}, {23, 29}, {52, 68}, {38, 52}, {23, 31},
                    {21, 27}, {82, 110}, {32, 46}, {24, 30}, {19, 23}, {71, 97}, {28, 48},
                    {30, 38}, {19, 29}, {46, 70}, {30, 42}, {21, 29}, {14, 22}, {37, 55},
                    {56, 80}, {67, 85}, {88, 132}, {11, 23}
            },
            // Letter 'L'
            {
                    {100, 100}, {47, 55}, {36, 40}, {23, 31}, {59, 71}, {41, 53}, {25, 33},
                    {20, 28}, {86, 114}, {23, 35}, {28, 40}, {23, 31}, {25, 43}, {11, 23},
                    {31, 39}, {18, 24}, {31, 55}, {16, 24}, {20, 28}, {12, 18}, {20, 34},
                    {121, 167}, {113, 161}, {21, 33}, {19, 25}
            },
            // Letter 'M'
            {
                    {100, 100}, {27, 35}, {15, 21}, {5, 21}, {20, 40}, {33, 45}, {26, 30},
                    {11, 15}, {53, 67}, {34, 53}, {28, 32}, {9, 13}, {60, 72}, {31, 45},
                    {22, 30}, {7, 11}, {53, 61}, {31, 41}, {14, 24}, {3, 7}, {44, 64},
                    {15, 39}, {12, 16}, {14, 22}, {17, 25}
            },
            // Letter 'N'
            {
                    {100, 100}, {26, 38}, {19, 23}, {17, 21}, {36, 42}, {29, 41}, {27, 31},
                    {13, 27}, {54, 70}, {33, 45}, {28, 32}, {9, 13}, {61, 73}, {37, 51},
                    {18, 28}, {2, 8}, {57, 69}, {34, 46}, {10, 22}, {1, 9}, {46, 56},
                    {33, 49}, {7, 19}, {17, 27}, {14, 22}
            },
            // Letter 'O'
            {
                    {100, 100}, {34, 46}, {27, 35}, {24, 30}, {53, 61}, {27, 35}, {14, 24},
                    {12, 20}, {40, 64}, {34, 42}, {17, 31}, {14, 24}, {57, 87}, {35, 45},
                    {19, 31}, {16, 24}, {62, 90}, {30, 38}, {20, 28}, {15, 23}, {62, 82},
                    {13, 25}, {8, 56}, {13, 19}, {17, 25}
            },
            // Letter 'P'
            {
                    {100, 100}, {37, 45}, {36, 44}, {29, 35}, {66, 78}, {52, 60}, {30, 38},
                    {24, 32}, {106, 130}, {43, 53}, {28, 32}, {19, 25}, {76, 92}, {36, 44},
                    {25, 31}, {15, 21}, {70, 78}, {26, 30}, {18, 24}, {13, 17}, {51, 63},
                    {71, 93}, {117, 149}, {8, 14}, {0, 16}
            },
            // Letter 'Q'
            {
                    {100, 100}, {37, 77}, {38, 68}, {34, 52}, {72, 120}, {67, 99}, {36, 58},
                    {28, 48}, {132, 204}, {51, 103}, {22, 42}, {18, 30}, {42, 98}, {47, 91},
                    {19, 39}, {17, 23}, {40, 90}, {34, 74}, {15, 33}, {14, 20}, {27, 79},
                    {134, 174}, {126, 172}, {12, 28}, {9, 29}
            },
            // Letter 'R'
            {
                    {100, 100}, {26, 42}, {23, 35}, {22, 30}, {44, 64}, {37, 41}, {26, 30},
                    {23, 27}, {86, 96}, {45, 51}, {25, 33}, {20, 28}, {93, 109}, {25, 49},
                    {18, 34}, {19, 27}, {15, 35}, {18, 32}, {20, 24}, {19, 23}, {31, 41},
                    {67, 103}, {8, 32}, {90, 142}, {10, 34}
            },
            // Letter 'S'
            {
                    {100, 100}, {42, 52}, {35, 43}, {27, 35}, {59, 71}, {33, 41}, {30, 38},
                    {13, 17}, {11, 17}, {25, 37}, {40, 44}, {8, 12}, {15, 23}, {23, 29},
                    {36, 44}, {7, 13}, {23, 27}, {20, 28}, {25, 29}, {7, 15}, {19, 25},
                    {28, 44}, {19, 27}, {18, 26}, {17, 23}
            },
            // Letter 'T'
            {
                    {100, 100}, {46, 54}, {37, 43}, {26, 34}, {64, 76}, {35, 43}, {18, 30},
                    {21, 25}, {1, 17}, {31, 37}, {35, 41}, {14, 26}, {23, 31}, {20, 24},
                    {35, 43}, {10, 20}, {33, 41}, {19, 25}, {23, 29}, {8, 14}, {21, 29},
                    {45, 53}, {21, 31}, {22, 30}, {18, 26}
            },
            // Letter 'U'
            {
                    {100, 100}, {31, 51}, {29, 41}, {25, 31}, {55, 69}, {40, 48}, {24, 28},
                    {20, 26}, {85, 101}, {46, 54}, {28, 32}, {22, 26}, {95, 111}, {15, 35},
                    {27, 39}, {20, 26}, {32, 40}, {12, 24}, {23, 31}, {17, 21}, {34, 54},
                    {73, 95}, {18, 22}, {126, 154}, {13, 29}
            },
            // Letter 'V'
            {
                    {100, 100}, {23, 39}, {28, 32}, {21, 29}, {50, 60}, {40, 46}, {24, 28},
                    {21, 25}, {86, 98}, {45, 51}, {26, 30}, {23, 37}, {95, 105}, {29, 33},
                    {25, 33}, {20, 24}, {17, 33}, {15, 23}, {19, 25}, {17, 21}, {20, 40},
                    {84, 132}, {47, 77}, {123, 137}, {19, 23}
            },
            // Letter 'W'
            {
                    {100, 100}, {24, 40}, {33, 37}, {27, 29}, {58, 64}, {39, 43}, {22, 26},
                    {20, 24}, {84, 90}, {42, 46}, {23, 37}, {19, 23}, {87, 95}, {35, 43},
                    {23, 27}, {20, 24}, {79, 93}, {19, 37}, {4, 16}, {6, 18}, {4, 36},
                    {81, 121}, {45, 57}, {21, 51}, {78, 98}
            },
            // Letter 'X'
            {
                    {100, 100}, {39, 47}, {37, 41}, {26, 30}, {63, 69}, {31, 35}, {4, 20},
                    {9, 17}, {36, 60}, {15, 27}, {40, 44}, {7, 25}, {33, 41}, {15, 19},
                    {37, 41}, {6, 18}, {27, 39}, {9, 17}, {26, 30}, {8, 12}, {22, 30},
                    {40, 60}, {77, 101}, {18, 26}, {19, 23}
            },
            // Letter 'Y'
            {
                    {100, 100}, {47, 63}, {38, 42}, {21, 33}, {58, 74}, {17, 35}, {26, 34},
                    {22, 26}, {33, 39}, {8, 24}, {34, 42}, {22, 30}, {49, 55}, {6, 18},
                    {31, 39}, {24, 28}, {45, 57}, {35, 41}, {23, 27}, {21, 29}, {80, 96},
                    {86, 124}, {17, 33}, {9, 17}, {124, 160}
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
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    };

    /** Use this when complete
    private char[] listAlpha = {
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    };
     */

    protected double[][][] getDataAlpha() {
        return dataAlpha;
    }

    protected  char[] getListAlpha() {
        return listAlpha;
    }
}
