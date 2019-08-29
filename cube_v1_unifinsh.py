import math
import time


class cube:
    def __init__(self):
        self.direction = ['U', 'L', 'F', 'R', 'B', 'D']
        self.status = [[self.direction[j] + str(i) for i in range(9)] for j in range(6)]
        self.color = ['white', 'orange', 'green', 'red', 'blue', 'yellow']

    def show_cube(self):
        # U
        for i in range(0, 7, 3):
            print('            |' + str(self.status[0][i]) + '|' + str(self.status[0][i + 1]) + '|' + str(
                self.status[0][i + 2]) + '|')
        # L F R B
        for i in range(0, 7, 3):
            temp = ""
            for face in range(1, 5):
                temp += ' |' + str(self.status[face][i]) + '|' + str(self.status[face][i + 1]) + '|' + str(
                    self.status[face][i + 2]) + '|'
            print(temp)
        # D
        for i in range(0, 7, 3):
            print('            |' + str(self.status[5][i]) + '|' + str(self.status[5][i + 1]) + '|' + str(
                self.status[5][i + 2]) + '|')

    # moves
    def face_move(self, face, mode):
        if mode == 1:
            self.status[face][1], self.status[face][5], self.status[face][7], self.status[face][3] = \
                self.status[face][3], self.status[face][1], self.status[face][5], self.status[face][7]
            self.status[face][0], self.status[face][2], self.status[face][8], self.status[face][6] = \
                self.status[face][6], self.status[face][0], self.status[face][2], self.status[face][8]
        if mode == 2:
            self.status[face][1], self.status[face][5], self.status[face][7], self.status[face][3] = \
                self.status[face][7], self.status[face][3], self.status[face][1], self.status[face][5]
            self.status[face][0], self.status[face][2], self.status[face][8], self.status[face][6] = \
                self.status[face][8], self.status[face][6], self.status[face][0], self.status[face][2]
        if mode == 3:
            self.status[face][1], self.status[face][5], self.status[face][7], self.status[face][3] = \
                self.status[face][5], self.status[face][7], self.status[face][3], self.status[face][1]
            self.status[face][0], self.status[face][2], self.status[face][8], self.status[face][6] = \
                self.status[face][2], self.status[face][8], self.status[face][6], self.status[face][0]

    def U(self):
        self.face_move(face=0, mode=1)
        for i in range(3):
            self.status[1][i], self.status[2][i], self.status[3][i], self.status[4][i] = \
                self.status[2][i], self.status[3][i], self.status[4][i], self.status[1][i]

    def U2(self):
        self.face_move(face=0, mode=2)
        for i in range(3):
            self.status[1][i], self.status[2][i], self.status[3][i], self.status[4][i] = \
                self.status[3][i], self.status[4][i], self.status[1][i], self.status[2][i]

    def U3(self):
        self.face_move(face=0, mode=3)
        for i in range(3):
            self.status[1][i], self.status[2][i], self.status[3][i], self.status[4][i] = \
                self.status[4][i], self.status[1][i], self.status[2][i], self.status[3][i]

    def L(self):
        self.face_move(face=1, mode=1)
        self.status[0][0], self.status[0][3], self.status[0][6], self.status[2][0], self.status[2][3], self.status[2][
            6], self.status[5][0], self.status[5][3], self.status[5][6], self.status[4][8], self.status[4][5], \
        self.status[4][2] = \
            self.status[4][8], self.status[4][5], self.status[4][2], self.status[0][0], self.status[0][3], \
            self.status[0][6], self.status[2][0], self.status[2][3], self.status[2][6], self.status[5][0], \
            self.status[5][3], self.status[5][6]

    def L2(self):
        self.face_move(face=1, mode=2)
        self.status[0][0], self.status[0][3], self.status[0][6], self.status[2][0], self.status[2][3], self.status[2][
            6], self.status[5][0], self.status[5][3], self.status[5][6], self.status[4][8], self.status[4][5], \
        self.status[4][2] = \
            self.status[5][0], self.status[5][3], self.status[5][6], self.status[4][8], self.status[4][5], \
            self.status[4][2], self.status[0][0], self.status[0][3], self.status[0][6], self.status[2][0], \
            self.status[2][3], self.status[2][6]

    def L3(self):
        self.face_move(face=1, mode=3)
        pass

    def F(self):
        self.face_move(face=2, mode=1)
        pass


    def F2(self):
        self.face_move(face=2, mode=2)
        pass


    def F3(self):
        self.face_move(face=2, mode=3)
        pass


    def R(self):
        self.face_move(face=3, mode=1)
        pass


    def R2(self):
        self.face_move(face=3, mode=2)
        pass


    def R3(self):
        self.face_move(face=3, mode=3)
        pass


    def B(self):
        self.face_move(face=4, mode=1)
        pass


    def B2(self):
        self.face_move(face=4, mode=2)
        pass


    def B3(self):
        self.face_move(face=4, mode=3)
        pass


    def D(self):
        self.face_move(face=5, mode=1)
        pass


    def D2(self):
        self.face_move(face=5, mode=2)
        pass


    def D3(self):
        self.face_move(face=5, mode=3)
        pass


test = cube()
# print(test.status)
test.show_cube()
test.L2()
print('-------------')
test.show_cube()
