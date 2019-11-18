class cube:
    def __init__(self, c_place=[i for i in range(8)], c_status=[0 for i in range(8)]):
        self.direction = ['U', 'L', 'F', 'R', 'B', 'D']
        self.c_place = c_place
        self.c_status = c_status
        self.c_standard = [['U', 'F', 'L'], ['U', 'L', 'B'], ['U', 'B', 'R'], ['U', 'R', 'F'], ['D', 'L', 'F'],
                           ['D', 'B', 'L'], ['D', 'R', 'B'], ['D', 'F', 'R']]
        self.color = ['white', 'orange', 'green', 'red', 'blue', 'yellow']
        self.move_map = {
            'U': self.U,
            'U2': self.U2,
            "U'": self.U3,
            'F': self.F,
            'F2': self.F2,
            "F'": self.F3,
            'R': self.R,
            'R2': self.R2,
            "R'": self.R3,
            "Q": self.reset,
        }

    def reset(self, c_place=[i for i in range(8)], c_status=[0 for i in range(8)]):
        self.c_place = c_place
        self.c_status = c_status

    def show_cube(self):
        '''
         1. 把存放角块棱块的四个数组的信息转化成六个面情况的信息
         2. 将面的信息以
               |U|U|
               |U|U|
         |L|L| |F|F| |R|R| |B|B|
         |L|L| |F|F| |R|R| |B|B|
               |D|D|
               |D|D|
            的格式打印出来
        '''

        # 根据转态将棱角信息转化到c,e中
        # e: 0-当前位置的棱块高级色朝向高级面|1-当前位置棱块的高级色朝向低级色
        # c: 0-角块高级色朝向高级面|1-角块高级色由高级面顺时针转1次|2-角块高级色由高级面顺时针转2次
        c = []
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
        # 再将c, e中的信息转化到cube中，cube分别代表魔方的6个面
        cube = [
            [c[1][0], c[2][0], c[0][0], c[3][0]],
            [c[1][1], c[0][2], c[5][2], c[4][1]],
            [c[0][1], c[3][2], c[4][2], c[7][1]],
            [c[3][1], c[2][2], c[7][2], c[6][1]],
            [c[2][1], c[1][2], c[6][2], c[5][1]],
            [c[4][0], c[7][0], c[5][0], c[6][0]],
        ]
        # 添加颜色
        for face in range(6):
            for cell in range(4):
                if cube[face][cell] == 'U':
                    cube[face][cell] = "\033[1;30;47m" + cube[face][cell] + "\033[0m"
                elif cube[face][cell] == 'L':
                    cube[face][cell] = "\033[1;30;45m" + cube[face][cell] + "\033[0m"
                elif cube[face][cell] == 'F':
                    cube[face][cell] = "\033[1;30;42m" + cube[face][cell] + "\033[0m"
                elif cube[face][cell] == 'R':
                    cube[face][cell] = "\033[1;30;41m" + cube[face][cell] + "\033[0m"
                elif cube[face][cell] == 'B':
                    cube[face][cell] = "\033[1;30;44m" + cube[face][cell] + "\033[0m"
                elif cube[face][cell] == 'D':
                    cube[face][cell] = "\033[1;30;43m" + cube[face][cell] + "\033[0m"
        # 打印
        # U
        for i in range(0, 3, 2):
            print('     |' + str(cube[0][i]) + '|' + str(cube[0][i + 1]) + '|')
        # L F R B
        for i in range(0, 3, 2):
            temp = ""
            for face in range(1, 5):
                temp += '|' + str(cube[face][i]) + '|' + str(cube[face][i + 1]) + '|'
            print(temp)
        # D
        for i in range(0, 3, 2):
            print('     |' + str(cube[5][i]) + '|' + str(cube[5][i + 1]) + '|')

    # MOVES
    def U(self):
        self.c_place[0], self.c_place[1], self.c_place[2], self.c_place[3] = self.c_place[3], self.c_place[0], self.c_place[1], self.c_place[2]
        self.c_status[0], self.c_status[1], self.c_status[2], self.c_status[3] = self.c_status[3], self.c_status[0], self.c_status[1], self.c_status[2]
    def U2(self):
        self.c_place[0], self.c_place[1], self.c_place[2], self.c_place[3] = self.c_place[2], self.c_place[3], self.c_place[0], self.c_place[1]
        self.c_status[0], self.c_status[1], self.c_status[2], self.c_status[3] = self.c_status[2], self.c_status[3], self.c_status[0], self.c_status[1]
    def U3(self):
        self.c_place[0], self.c_place[1], self.c_place[2], self.c_place[3] = self.c_place[1], self.c_place[2], self.c_place[3], self.c_place[0]
        self.c_status[0], self.c_status[1], self.c_status[2], self.c_status[3] = self.c_status[1], self.c_status[2], self.c_status[3], self.c_status[0]
    def F(self):
        self.c_place[0], self.c_place[3], self.c_place[7], self.c_place[4] = self.c_place[4], self.c_place[0], self.c_place[3], self.c_place[7]
        self.c_status[0], self.c_status[3], self.c_status[7], self.c_status[4] = (self.c_status[4] + 2) % 3, (self.c_status[0] + 1) % 3, (self.c_status[3] + 2) % 3, (self.c_status[7] + 1) % 3
    def F2(self):
        self.c_place[0], self.c_place[3], self.c_place[7], self.c_place[4] = self.c_place[7], self.c_place[4], self.c_place[0], self.c_place[3]
        self.c_status[0], self.c_status[3], self.c_status[7], self.c_status[4] = self.c_status[7], self.c_status[4], self.c_status[0], self.c_status[3]
    def F3(self):
        self.c_place[0], self.c_place[3], self.c_place[7], self.c_place[4] = self.c_place[3], self.c_place[7], self.c_place[4], self.c_place[0]
        self.c_status[0], self.c_status[3], self.c_status[7], self.c_status[4] = (self.c_status[3] + 2) % 3, (self.c_status[7] + 1) % 3, (self.c_status[4] + 2) % 3, (self.c_status[0] + 1) % 3
    def R(self):
        self.c_place[3], self.c_place[2], self.c_place[6], self.c_place[7] = self.c_place[7], self.c_place[3], self.c_place[2], self.c_place[6]
        self.c_status[3], self.c_status[2], self.c_status[6], self.c_status[7] = (self.c_status[7] + 2) % 3, (self.c_status[3] + 1) % 3, (self.c_status[2] + 2) % 3, (self.c_status[6] + 1) % 3
    def R2(self):
        self.c_place[3], self.c_place[2], self.c_place[6], self.c_place[7] = self.c_place[6], self.c_place[7], self.c_place[3], self.c_place[2]
        self.c_status[3], self.c_status[2], self.c_status[6], self.c_status[7] = self.c_status[6], self.c_status[7], self.c_status[3], self.c_status[2]
    def R3(self):
        self.c_place[3], self.c_place[2], self.c_place[6], self.c_place[7] = self.c_place[2], self.c_place[6], self.c_place[7], self.c_place[3]
        self.c_status[3], self.c_status[2], self.c_status[6], self.c_status[7] = (self.c_status[2] + 2) % 3, (self.c_status[6] + 1) % 3, (self.c_status[7] + 2) % 3, (self.c_status[3] + 1) % 3

    def one_move(self, move):
        self.move_map[move]()

    def get_moves(self, getinput):
        move = getinput.upper().replace(' ', '')
        moves = []
        if len(move) > 1:
            for i in range(1, len(move)):
                if move[i] == "2" or move[i] == "'":
                    moves.append(move[i - 1:i + 1])
                elif i < len(move) - 1 and move[i - 1] != "'" and move[i - 1] != "2":
                    moves.append(move[i - 1])
                elif i == len(move) - 1:
                    if move[i - 1] != "'" and move[i - 1] != "2":
                        moves.append(move[i - 1])
                    moves.append(move[i])
        else:
            moves = [move]
        return moves

    # 判断是否符合目标状态
    def is_status_finish(self):
        # if self.c_status == [0 for i in range(8)] and self.c_place == [i for i in range(8)]:
        if self.c_status == [0 for i in range(8)]:
            return True
        else:
            return False

    def is_all_finish(self):
        if self.c_status == [0 for i in range(8)] and self.c_place == [i for i in range(8)]:
            return True
        else:
            return False

