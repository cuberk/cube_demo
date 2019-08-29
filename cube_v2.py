import math
import time


class cube:
    def __init__(self):
        self.direction = ['U', 'L', 'F', 'R', 'B', 'D']
        self.e_place = [i for i in range(12)]  # 棱块位置
        self.e_status = [0 for i in range(12)]  # 棱块朝向
        self.c_place = [i for i in range(8)]  # 角块位置
        self.c_status = [0 for i in range(8)]  # 角块朝向
        self.e_standard = [['U', 'F'], ['U', 'L'], ['U', 'B'], ['U', 'R'], ['D', 'F'], ['D', 'L'], ['D', 'B'],
                           ['D', 'R'], ['F', 'L'], ['B', 'L'], ['B', 'R'], ['F', 'R']]
        self.c_standard = [['U', 'F', 'L'], ['U', 'L', 'B'], ['U', 'B', 'R'], ['U', 'R', 'F'], ['D', 'L', 'F'],
                           ['D', 'B', 'L'], ['D', 'R', 'B'], ['D', 'F', 'R']]
        self.color = ['white', 'orange', 'green', 'red', 'blue', 'yellow']

    def show_cube(self):
        '''
         1. 把存放角块棱块的四个数组的信息转化成六个面情况的信息
         2. 将面的信息以
                 |U|U|U|
                 |U|U|U|
                 |U|U|U|
         |L|L|L| |F|F|F| |R|R|R| |B|B|B|
         |L|L|L| |F|F|F| |R|R|R| |B|B|B|
         |L|L|L| |F|F|F| |R|R|R| |B|B|B|
                 |D|D|D|
                 |D|D|D|
                 |D|D|D|
            的格式打印出来
        '''
        e, c = [], []
        for i in range(12):
            if self.e_status[i] == 0:
                e.append([self.e_standard[self.e_place[i]][0], self.e_standard[self.e_place[i]][1]])
            if self.e_status[i] == 1:
                e.append([self.e_standard[self.e_place[i]][1], self.e_standard[self.e_place[i]][0]])
        for i in range(8):
            if self.c_status[i] == 0:
                c.append([self.c_standard[self.c_place[i]][0], self.c_standard[self.c_place[i]][1],
                          self.c_standard[self.c_place[i]][2]])
            if self.c_status[i] == 1:
                c.append([self.c_standard[self.c_place[i]][2], self.c_standard[self.c_place[i]][0],
                          self.c_standard[self.c_place[i]][1]])
            if self.c_status[i] == 2:
                c.append([self.c_standard[self.c_place[i]][1], self.c_standard[self.c_place[i]][2],
                          self.c_standard[self.c_place[i]][0]])
        board = [
            [c[1][0], e[2][0], c[2][0], e[1][0], 'U', e[3][0], c[0][0], e[0][0], c[3][0]],
            [c[1][1], e[1][1], c[0][2], e[9][1], 'L', e[8][1], c[5][2], e[5][1], c[4][1]],
            [c[0][1], e[0][1], c[3][2], e[8][0], 'F', e[11][0], c[4][2], e[4][1], c[7][1]],
            [c[3][1], e[3][1], c[2][2], e[11][1], 'R', e[10][1], c[7][2], e[7][1], c[6][1]],
            [c[2][1], e[2][1], c[1][2], e[10][0], 'B', e[9][0], c[6][2], e[6][1], c[5][1]],
            [c[4][0], e[4][0], c[7][0], e[5][0], 'D', e[7][0], c[5][0], e[6][0], c[6][0]],
        ]
        # U
        for i in range(0, 7, 3):
            print('         |' + str(board[0][i]) + '|' + str(board[0][i + 1]) + '|' + str(
                board[0][i + 2]) + '|')
        # L F R B
        for i in range(0, 7, 3):
            temp = ""
            for face in range(1, 5):
                temp += ' |' + str(board[face][i]) + '|' + str(board[face][i + 1]) + '|' + str(
                    board[face][i + 2]) + '|'
            print(temp)
        # D
        for i in range(0, 7, 3):
            print('         |' + str(board[5][i]) + '|' + str(board[5][i + 1]) + '|' + str(
                board[5][i + 2]) + '|')
        print(self.e_place)
        print(self.e_status)
        print(self.c_place)
        print(self.c_status)

    # MOVES
    def U(self):
        self.e_place[0], self.e_place[1], self.e_place[2], self.e_place[3] = self.e_place[3], self.e_place[0], self.e_place[1], self.e_place[2]
        self.e_status[0], self.e_status[1], self.e_status[2], self.e_status[3] = self.e_status[3], self.e_status[0], self.e_status[1], self.e_status[2]
        self.c_place[0], self.c_place[1], self.c_place[2], self.c_place[3] = self.c_place[3], self.c_place[0], self.c_place[1], self.c_place[2]
        self.c_status[0], self.c_status[1], self.c_status[2], self.c_status[3] = self.c_status[3], self.c_status[0], self.c_status[1], self.c_status[2]
    def U2(self):
        self.e_place[0], self.e_place[1], self.e_place[2], self.e_place[3] = self.e_place[2], self.e_place[3], self.e_place[0], self.e_place[1]
        self.e_status[0], self.e_status[1], self.e_status[2], self.e_status[3] = self.e_status[2], self.e_status[3], self.e_status[0], self.e_status[1]
        self.c_place[0], self.c_place[1], self.c_place[2], self.c_place[3] = self.c_place[2], self.c_place[3], self.c_place[0], self.c_place[1]
        self.c_status[0], self.c_status[1], self.c_status[2], self.c_status[3] = self.c_status[2], self.c_status[3], self.c_status[0], self.c_status[1]
    def U3(self):
        self.e_place[0], self.e_place[1], self.e_place[2], self.e_place[3] = self.e_place[1], self.e_place[2], self.e_place[3], self.e_place[0]
        self.e_status[0], self.e_status[1], self.e_status[2], self.e_status[3] = self.e_status[1], self.e_status[2], self.e_status[3], self.e_status[0]
        self.c_place[0], self.c_place[1], self.c_place[2], self.c_place[3] = self.c_place[1], self.c_place[2], self.c_place[3], self.c_place[0]
        self.c_status[0], self.c_status[1], self.c_status[2], self.c_status[3] = self.c_status[1], self.c_status[2], self.c_status[3], self.c_status[0]
    def L(self):
        self.e_place[1], self.e_place[8], self.e_place[5], self.e_place[9] = self.e_place[9], self.e_place[1], self.e_place[8], self.e_place[5]
        self.e_status[1], self.e_status[8], self.e_status[5], self.e_status[9] = self.e_status[9], self.e_status[1], self.e_status[8], self.e_status[5]
        self.c_place[0], self.c_place[4], self.c_place[5], self.c_place[1] = self.c_place[1], self.c_place[0], self.c_place[4], self.c_place[5]
        self.c_status[0], self.c_status[4], self.c_status[5], self.c_status[1] = (self.c_status[1] + 1) % 3, (self.c_status[0] + 2) % 3, (self.c_status[4] + 1) % 3, (self.c_status[5] + 2) % 3
    def L2(self):
        self.e_place[1], self.e_place[8], self.e_place[5], self.e_place[9] = self.e_place[5], self.e_place[9], self.e_place[1], self.e_place[8]
        self.e_status[1], self.e_status[8], self.e_status[5], self.e_status[9] = self.e_status[5], self.e_status[9], self.e_status[1], self.e_status[8]
        self.c_place[0], self.c_place[4], self.c_place[5], self.c_place[1] = self.c_place[5], self.c_place[1], self.c_place[0], self.c_place[4]
        self.c_status[0], self.c_status[4], self.c_status[5], self.c_status[1] = self.c_status[5], self.c_status[1], self.c_status[0], self.c_status[4]
    def L3(self):
        self.e_place[1], self.e_place[8], self.e_place[5], self.e_place[9] = self.e_place[8], self.e_place[5], self.e_place[9], self.e_place[1]
        self.e_status[1], self.e_status[8], self.e_status[5], self.e_status[9] = self.e_status[8], self.e_status[5], self.e_status[9], self.e_status[1]
        self.c_place[0], self.c_place[4], self.c_place[5], self.c_place[1] = self.c_place[4], self.c_place[5], self.c_place[1], self.c_place[0]
        self.c_status[0], self.c_status[4], self.c_status[5], self.c_status[1] = (self.c_status[4] + 1) % 3, (self.c_status[5] + 2) % 3, (self.c_status[1] + 1) % 3, (self.c_status[0] + 2) % 3
    def F(self):
        self.e_place[0], self.e_place[11], self.e_place[4], self.e_place[8] = self.e_place[8], self.e_place[0], self.e_place[11], self.e_place[4]
        self.e_status[0], self.e_status[11], self.e_status[4], self.e_status[8] = (self.e_status[8] + 1) % 2, (self.e_status[0] + 1) % 2, (self.e_status[11] + 1) % 2, (self.e_status[4] + 1) % 2
        self.c_place[0], self.c_place[3], self.c_place[7], self.c_place[4] = self.c_place[4], self.c_place[0], self.c_place[3], self.c_place[7]
        self.c_status[0], self.c_status[3], self.c_status[7], self.c_status[4] = (self.c_status[4] + 2) % 3, (self.c_status[0] + 1) % 3, (self.c_status[3] + 2) % 3, (self.c_status[7] + 1) % 3
    def F2(self):
        self.e_place[0], self.e_place[11], self.e_place[4], self.e_place[8] = self.e_place[4], self.e_place[8], self.e_place[0], self.e_place[11]
        self.e_status[0], self.e_status[11], self.e_status[4], self.e_status[8] = self.e_status[4], self.e_status[8], self.e_status[0], self.e_status[11]
        self.c_place[0], self.c_place[3], self.c_place[7], self.c_place[4] = self.c_place[7], self.c_place[4], self.c_place[0], self.c_place[3]
        self.c_status[0], self.c_status[3], self.c_status[7], self.c_status[4] = self.c_status[7], self.c_status[4], self.c_status[0], self.c_status[3]
    def F3(self):
        self.e_place[0], self.e_place[11], self.e_place[4], self.e_place[8] = self.e_place[11], self.e_place[4], self.e_place[8], self.e_place[0]
        self.e_status[0], self.e_status[11], self.e_status[4], self.e_status[8] = (self.e_status[11] + 1) % 2, (self.e_status[4] + 1) % 2, (self.e_status[8] + 1) % 2, (self.e_status[0] + 1) % 2
        self.c_place[0], self.c_place[3], self.c_place[7], self.c_place[4] = self.c_place[3], self.c_place[7], self.c_place[4], self.c_place[0]
        self.c_status[0], self.c_status[3], self.c_status[7], self.c_status[4] = (self.c_status[3] + 2) % 3, (self.c_status[7] + 1) % 3, (self.c_status[4] + 2) % 3, (self.c_status[0] + 1) % 3
    def R(self):
        self.e_place[3], self.e_place[10], self.e_place[7], self.e_place[11] = self.e_place[11], self.e_place[3], self.e_place[10], self.e_place[7]
        self.e_status[3], self.e_status[10], self.e_status[7], self.e_status[11] = self.e_status[11], self.e_status[3], self.e_status[10], self.e_status[7]
        self.c_place[3], self.c_place[2], self.c_place[6], self.c_place[7] = self.c_place[7], self.c_place[3], self.c_place[2], self.c_place[6]
        self.c_status[3], self.c_status[2], self.c_status[6], self.c_status[7] = (self.c_status[7] + 2) % 3, (self.c_status[3] + 1) % 3, (self.c_status[2] + 2) % 3, (self.c_status[6] + 1) % 3
    def R2(self):
        self.e_place[3], self.e_place[10], self.e_place[7], self.e_place[11] = self.e_place[7], self.e_place[11], self.e_place[3], self.e_place[10]
        self.e_status[3], self.e_status[10], self.e_status[7], self.e_status[11] = self.e_status[7], self.e_status[11], self.e_status[3], self.e_status[10]
        self.c_place[3], self.c_place[2], self.c_place[6], self.c_place[7] = self.c_place[6], self.c_place[7], self.c_place[3], self.c_place[2]
        self.c_status[3], self.c_status[2], self.c_status[6], self.c_status[7] = self.c_status[6], self.c_status[7], self.c_status[3], self.c_status[2]
    def R3(self):
        self.e_place[3], self.e_place[10], self.e_place[7], self.e_place[11] = self.e_place[10], self.e_place[7], self.e_place[11], self.e_place[3]
        self.e_status[3], self.e_status[10], self.e_status[7], self.e_status[11] = self.e_status[10], self.e_status[7], self.e_status[11], self.e_status[3]
        self.c_place[3], self.c_place[2], self.c_place[6], self.c_place[7] = self.c_place[2], self.c_place[6], self.c_place[7], self.c_place[3]
        self.c_status[3], self.c_status[2], self.c_status[6], self.c_status[7] = (self.c_status[2] + 2) % 3, (self.c_status[6] + 1) % 3, (self.c_status[7] + 2) % 3, (self.c_status[3] + 1) % 3
    def B(self):
        self.e_place[2], self.e_place[9], self.e_place[6], self.e_place[10] = self.e_place[10], self.e_place[2], self.e_place[9], self.e_place[6]
        self.e_status[2], self.e_status[9], self.e_status[6], self.e_status[10] = (self.e_status[10] + 1) % 2, (self.e_status[2] + 1) % 2, (self.e_status[9] + 1) % 2, (self.e_status[6] + 1) % 2
        self.c_place[2], self.c_place[1], self.c_place[5], self.c_place[6] = self.c_place[6], self.c_place[2], self.c_place[1], self.c_place[5]
        self.c_status[2], self.c_status[1], self.c_status[5], self.c_status[6] = (self.c_status[6] + 2) % 3, (self.c_status[2] + 1) % 3, (self.c_status[1] + 2) % 3, (self.c_status[5] + 1) % 3
    def B2(self):
        self.e_place[2], self.e_place[9], self.e_place[6], self.e_place[10] = self.e_place[6], self.e_place[10], self.e_place[2], self.e_place[9]
        self.e_status[2], self.e_status[9], self.e_status[6], self.e_status[10] = self.e_status[6], self.e_status[10], self.e_status[2], self.e_status[9]
        self.c_place[2], self.c_place[1], self.c_place[5], self.c_place[6] = self.c_place[5], self.c_place[6], self.c_place[2], self.c_place[1]
        self.c_status[2], self.c_status[1], self.c_status[5], self.c_status[6] = self.c_status[5], self.c_status[6], self.c_status[2], self.c_status[1]
    def B3(self):
        self.e_place[2], self.e_place[9], self.e_place[6], self.e_place[10] = self.e_place[9], self.e_place[6], self.e_place[10], self.e_place[2]
        self.e_status[2], self.e_status[9], self.e_status[6], self.e_status[10] = (self.e_status[9] + 1) % 2, (self.e_status[6] + 1) % 2, (self.e_status[10] + 1) % 2, (self.e_status[2] + 1) % 2
        self.c_place[2], self.c_place[1], self.c_place[5], self.c_place[6] = self.c_place[1], self.c_place[5],  self.c_place[6], self.c_place[2]
        self.c_status[2], self.c_status[1], self.c_status[5], self.c_status[6] = (self.c_status[1] + 2) % 3, (self.c_status[5] + 1) % 3, (self.c_status[6] + 2) % 3, (self.c_status[2] + 1) % 3
    def D(self):
        self.e_place[4], self.e_place[7], self.e_place[6], self.e_place[5] = self.e_place[5], self.e_place[4], self.e_place[7], self.e_place[6]
        self.e_status[4], self.e_status[7], self.e_status[6], self.e_status[5] = self.e_status[5], self.e_status[4], self.e_status[7], self.e_status[6]
        self.c_place[4], self.c_place[7], self.c_place[6], self.c_place[5] = self.c_place[5], self.c_place[4], self.c_place[7], self.c_place[6]
        self.c_status[4], self.c_status[7], self.c_status[6], self.c_status[5] = self.c_status[5], self.c_status[4], self.c_status[7], self.c_status[6]
    def D2(self):
        self.e_place[4], self.e_place[7], self.e_place[6], self.e_place[5] = self.e_place[6], self.e_place[5], self.e_place[4], self.e_place[7]
        self.e_status[4], self.e_status[7], self.e_status[6], self.e_status[5] = self.e_status[6], self.e_status[5], self.e_status[4], self.e_status[7]
        self.c_place[4], self.c_place[7], self.c_place[6], self.c_place[5] = self.c_place[6], self.c_place[5], self.c_place[4], self.c_place[7]
        self.c_status[4], self.c_status[7], self.c_status[6], self.c_status[5] = self.c_status[6], self.c_status[5], self.c_status[4], self.c_status[7]
    def D3(self):
        self.e_place[4], self.e_place[7], self.e_place[6], self.e_place[5] = self.e_place[7], self.e_place[6], self.e_place[5], self.e_place[4],
        self.e_status[4], self.e_status[7], self.e_status[6], self.e_status[5] = self.e_status[7], self.e_status[6], self.e_status[5], self.e_status[4]
        self.c_place[4], self.c_place[7], self.c_place[6], self.c_place[5] = self.c_place[7], self.c_place[6], self.c_place[5], self.c_place[4],
        self.c_status[4], self.c_status[7], self.c_status[6], self.c_status[5] = self.c_status[7], self.c_status[6], self.c_status[5], self.c_status[4]


test = cube()
# print(test.status)
for i in range(6):
    test.R()
    test.U()
    test.R3()
    test.U3()
    test.show_cube()
