import numpy as np
import pandas as pd


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1.0 - x)


num_to_alpha = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z',
}

alpha_to_num = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
}


class NeuralNet:
    def __init__(self, X, y):
        self.X = X
        self.y = y

        self.inputs = np.zeros(150)
        self.layers = np.array([130, 26])
        self.outputs = np.zeros(26)
        self.learning_rate = 0.03
        self.momentum = 0.9
        self.error_epsilon = 0.0015
        self.decay = False
        self.shuffle = True
        self.normalize = True

        # Layers
        self.weight_1 = np.array(np.random.rand(self.inputs.shape[0], self.layers[0]))
        self.weight_2 = np.array(np.random.rand(self.layers[0], self.layers[1]))
        self.weight_3 = np.array(np.random.rand(self.layers[1], self.outputs.shape[0]))
        print('Before Weight 1\n', self.weight_1.shape, '\n')
        print('Before Weight 2\n', self.weight_2.shape, '\n')
        print('Before Weight 3\n', self.weight_3.shape, '\n')

    def epoch(self, epoch):
        self.epoch = epoch  # 1000
        for i in range(self.epoch):
            for j, each_x in enumerate(self.X):
                self.feedforward(each_x)
                self.backprop(each_x, self.y[j])


    def feedforward(self, each_x):
        self.final_output = []
        self.layer_1 = sigmoid(np.dot(each_x, self.weight_1))
        self.layer_2 = sigmoid(np.dot(self.layer_1, self.weight_2))
        self.output = sigmoid(np.dot(self.layer_2, self.weight_3))
        # print(self.layer_1.shape, each_x.shape, self.weight_1.shape)
        # print(self.layer_2.shape, self.layer_1.shape, self.weight_2.shape)
        # print(self.output.shape, self.layer_2.shape, self.weight_3.shape)

        # print(self.layer_1)
        # print(self.layer_2)
        # print(self.output)
        # print()
        # index = np.argmax(self.output)
        # max = np.amax(self.output)
        # print(index, max)
        # self.final_output.append([np.argmax(self.output), np.amax(self.output)])

        """
        for each_row in self.X:
            self.layer_1 = sigmoid(np.dot(each_row, self.weight_1))
            self.layer_2 = sigmoid(np.dot(self.layer_1, self.weight_2))
            self.output = sigmoid(np.dot(self.layer_2, self.weight_3))
            # print(self.layer_1)
            # print(self.layer_2)
            # print(self.output)
            # print()
            # index = np.argmax(self.output)
            # max = np.amax(self.output)
            # print(index, max)
            self.final_output.append([np.argmax(self.output), np.amax(self.output)])
        self.final_output = np.array(self.final_output)
        # print(self.final_output)
        """

    def backprop(self, each_x, each_y):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        temp = self.learning_rate * (each_y - self.output) * sigmoid_derivative(self.output)
        print(self.layer_2.T.shape, temp.shape)
        print('Temp 1\n', temp, '\n')
        d_weights_3 = np.dot(self.layer_2.T, temp)

        temp = np.dot(temp, self.weight_3.T) * sigmoid_derivative(self.layer_2)
        print(self.weight_3.T.shape, self.layer_2.shape)
        print('Temp 2\n', temp, '\n')
        d_weights_2 = np.dot(self.layer_1.T, temp)

        temp = np.dot(temp, self.weight_2.T) * sigmoid_derivative(self.layer_1)
        print(temp)
        print('Temp 3\n', temp, '\n')
        d_weights_1 = np.dot(each_x.T, temp)

        # update the weights with the derivative (slope) of the loss function
        self.weight_1 += d_weights_1
        self.weight_2 += d_weights_2
        self.weight_3 += d_weights_3

        # print('Epoch ', epoch)
        # print('Weight 1\n', self.weight_1, '\n')
        # print('Weight 2\n', self.weight_2, '\n')
        # print('Weight 3\n', self.weight_3, '\n')

        # print('d_weights_1\n', d_weights_1, '\n')
        # print('d_weights_2\n', d_weights_2, '\n')
        # print()


"""
if __name__ == "__main__":
    X = np.array([[0,0,1],
                  [0,1,1],
                  [1,0,1],
                  [1,1,1]])
    y = np.array([[0],[1],[1],[0]])
    nn = NeuralNet(X,y)

    for i in range(1500):
        nn.feedforward()
        nn.backprop()

    print(nn.output)
"""
if __name__ == "__main__":
    data = pd.read_csv(r'.\HandRecBaseV4_output\data\hand_sign_data_hasif.csv')

    actual_output = data['Actual Output'].to_numpy()
    y = np.zeros(shape=[data.shape[0], 26])

    for i, y_each in enumerate(actual_output):
        index = alpha_to_num[y_each]
        y[i][index] = 1

    """
    for aplha in data['Actual Output']:
        y.append(alpha_to_num[aplha])
    y = np.array(y)
    """

    data = data.drop(['Actual Output'], axis=1)
    X = data.to_numpy()

    nn = NeuralNet(X, y)
    nn.epoch(1)
"""
    self.inputs = [[0] * 150]
    self.layer = [130, 26]
    self.weight = []
    self.epoch = 1000
    self.learning_rate = 0.03
    self.momentum = 0.9
    self.error_epsilon = 0.0015
    self.decay = False
    self.shuffle = True
    self.normalize = True
    text_file = "NeuralNet_info.txt"
    if os.path.isfile(os.path.join(r'.\\', text_file)):
        print("File Found")
        f = open(os.path.join(r'.\\', text_file), "r")
        lines = f.readlines()
        data = ""
        self.layer = []
        for line in lines:
            if line.split('=')[0] == 'hidden_layer':
                data = line.split('=')[1].split('\n')[0].split(',')
                for each in data:
                    self.layer.append(int(each))
                print("hidden_layer\t: ", self.layer)
            elif line.split('=')[0] == 'epoch':
                data = line.split('=')[1].split('\n')[0]
                self.epoch = int(data)
                print("Epoch\t\t\t: ", self.epoch)
            elif line.split('=')[0] == 'learning_rate':
                data = line.split('=')[1].split('\n')[0]
                self.learning_rate = float(data)
                print("learning_rate\t: ", self.learning_rate)
            elif line.split('=')[0] == 'error_epsilon':
                data = line.split('=')[1].split('\n')[0]
                self.error_epsilon = float(data)
                print("error_epsilon\t: ", self.error_epsilon)
            elif line.split('=')[0] == 'decay':
                data = line.split('=')[1].split('\n')[0]
                self.decay = bool(data)
                print("decay\t\t\t: ", self.decay)
            elif line.split('=')[0] == 'shuffle':
                data = line.split('=')[1].split('\n')[0]
                self.shuffle = bool(data)
                print("shuffle\t\t\t: ", self.shuffle)
            elif line.split('=')[0] == 'normalize':
                data = line.split('=')[1].split('\n')[0]
                self.normalize = bool(data)
                print("normalize\t\t: ", self.normalize)
            elif line.split('=')[0] == 'weight':
                weight_empty = False
                data = line.split('=')[1].split('\n')[0].replace('[', '', 2).replace(']', '').split(',[')
                temp = []
                temp_2 = []
                try:
                    for i in range(0, len(data)):
                        str_weight = data[i].split(',')
                        temp = []
                        if not str_weight:
                            print("Empty")
                            weight_empty = True
                            break
                        else:
                            # If None, Import Weight
                            for each_weight in str_weight:
                                temp.append(float(each_weight))
                            self.weight.append(temp)
                except:
                    weight_empty = True
                for i in range(0, len(self.layer)):
                    for j in range(0, self.layer[i]):
                        for k in range(0, len(self.inputs)):
                            temp_2.append(random.uniform(-10, 10))
                        temp.append(temp_2)
                    self.weight.append(temp)
                print("weight\t\t\t: ", self.weight)
    else:
        print("File Not Found")
        print("hidden_layer\t: ", self.layer)
        print("Epoch\t\t\t: ", self.epoch)
        print("learning_rate\t: ", self.learning_rate)
        print("error_epsilon\t: ", self.error_epsilon)
        print("decay\t\t\t: ", self.decay)
        print("shuffle\t\t\t: ", self.shuffle)
        print("normalize\t\t: ", self.normalize)
        temp = []
        temp_2 = []
        # Init Weight
        for i in range(0, len(self.layer)):
            for j in range(0, self.layer[i]):
                for k in range(0, len(self.inputs)):
                    temp_2.append(random.uniform(-10, 10))
                temp.append(temp_2)
            self.weight.append(temp)
        print("weight\t\t\t: ", self.weight)
"""
