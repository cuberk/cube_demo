from abc import ABC

from cube.Base import Base


class Three(Base, ABC):

    def init_cube(self):
        self.cubeRules = {
            "EP": {
                "length": 12,
                "min": 0,
                "max": 11,
                "isRepeat": 0,
                "default": list(range(12)),
            },
            "ES": {
                "length": 12,
                "min": 0,
                "max": 1,
                "isRepeat": 1,
                "default": [0 for i in range(12)],
            },
            "CP": {
                "length": 8,
                "min": 0,
                "max": 7,
                "isRepeat": 0,
                "default": list(range(8)),
            },
            "CS": {
                "length": 8,
                "min": 0,
                "max": 2,
                "isRepeat": 1,
                "default": [0 for i in range(8)],
            }
        }
        self.cube["EP"] = self.cubeRules["EP"]["default"][::]
        self.cube["ES"] = self.cubeRules["ES"]["default"][::]
        self.cube["CP"] = self.cubeRules["CP"]["default"][::]
        self.cube["CS"] = self.cubeRules["CS"]["default"][::]

    def init_moves(self):
        self.moves["R"] = self.moves_r
        self.moves["R2"] = self.moves_r2
        self.moves["R'"] = self.moves_r3
        self.moves["U"] = self.moves_u
        self.moves["U2"] = self.moves_u2
        self.moves["U'"] = self.moves_u3
        self.moves["F"] = self.moves_f
        self.moves["F2"] = self.moves_f2
        self.moves["F'"] = self.moves_f3
        self.moves["L"] = self.moves_l
        self.moves["L2"] = self.moves_l2
        self.moves["L'"] = self.moves_l3
        self.moves["D"] = self.moves_d
        self.moves["D2"] = self.moves_d2
        self.moves["D'"] = self.moves_d3
        self.moves["B"] = self.moves_b
        self.moves["B2"] = self.moves_b2
        self.moves["B'"] = self.moves_b3

    # todo 未完成
    def check_before_set(self, cube):
        for c in cube:
            if c not in self.cubeRules:
                return False
            if self.cubeRules[c]["length"] != len(c):
                return False
            for temp in c:
                if temp > self.cubeRules[c]["max"] or temp < self.cubeRules[c]["min"]:
                    return False
                if not self.cubeRules[c]["isRepeat"]:
                    # todo
                    pass
        return True

    def set_cube(self, cube):
        if self.check_before_set(cube):
            self.cube["EP"] = cube["EP"][::]
            self.cube["ES"] = cube["ES"][::]
            self.cube["CP"] = cube["CP"][::]
            self.cube["EP"] = cube["CS"][::]
        else:
            print("设定的魔方状态有问题")

    def draw_cube(self):
        e_standard = [['U', 'F'], ['U', 'L'], ['U', 'B'], ['U', 'R'], ['D', 'F'], ['D', 'L'], ['D', 'B'],
                      ['D', 'R'], ['F', 'L'], ['B', 'L'], ['B', 'R'], ['F', 'R']]
        c_standard = [['U', 'F', 'L'], ['U', 'L', 'B'], ['U', 'B', 'R'], ['U', 'R', 'F'], ['D', 'L', 'F'],
                      ['D', 'B', 'L'], ['D', 'R', 'B'], ['D', 'F', 'R']]
        
        # 根据转态将棱角信息转化到c,e中
        # e: 0-当前位置的棱块高级色朝向高级面|1-当前位置棱块的高级色朝向低级色
        # c: 0-角块高级色朝向高级面|1-角块高级色由高级面顺时针转1次|2-角块高级色由高级面顺时针转2次
        e, c = [], []
        for i in range(12):
            if self.cube["ES"][i] == 0:
                e.append([e_standard[self.cube["EP"][i]][0], e_standard[self.cube["EP"][i]][1]])
            if self.cube["ES"][i] == 1:
                e.append([e_standard[self.cube["EP"][i]][1], e_standard[self.cube["EP"][i]][0]])
        for i in range(8):
            if self.cube["CS"][i] == 0:
                c.append([c_standard[self.cube["CP"][i]][0], c_standard[self.cube["CP"][i]][1],
                          c_standard[self.cube["CP"][i]][2]])
            if self.cube["CS"][i] == 1:
                c.append([c_standard[self.cube["CP"][i]][2], c_standard[self.cube["CP"][i]][0],
                          c_standard[self.cube["CP"][i]][1]])
            if self.cube["CS"][i] == 2:
                c.append([c_standard[self.cube["CP"][i]][1], c_standard[self.cube["CP"][i]][2],
                          c_standard[self.cube["CP"][i]][0]])

        # 再将c, e中的信息转化到cube中，cube分别代表魔方的6个面
        cube = [
            [c[1][0], e[2][0], c[2][0], e[1][0], 'U', e[3][0], c[0][0], e[0][0], c[3][0]],
            [c[1][1], e[1][1], c[0][2], e[9][1], 'L', e[8][1], c[5][2], e[5][1], c[4][1]],
            [c[0][1], e[0][1], c[3][2], e[8][0], 'F', e[11][0], c[4][2], e[4][1], c[7][1]],
            [c[3][1], e[3][1], c[2][2], e[11][1], 'R', e[10][1], c[7][2], e[7][1], c[6][1]],
            [c[2][1], e[2][1], c[1][2], e[10][0], 'B', e[9][0], c[6][2], e[6][1], c[5][1]],
            [c[4][0], e[4][0], c[7][0], e[5][0], 'D', e[7][0], c[5][0], e[6][0], c[6][0]],
        ]

        # 添加颜色
        for face in range(6):
            for cell in range(9):
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
        for i in range(0, 7, 3):
            print('         |' + str(cube[0][i]) + '|' + str(cube[0][i + 1]) + '|' + str(
                cube[0][i + 2]) + '|')
        # L F R B
        for i in range(0, 7, 3):
            temp = ""
            for face in range(1, 5):
                temp += ' |' + str(cube[face][i]) + '|' + str(cube[face][i + 1]) + '|' + str(
                    cube[face][i + 2]) + '|'
            print(temp)
        # D
        for i in range(0, 7, 3):
            print('         |' + str(cube[5][i]) + '|' + str(cube[5][i + 1]) + '|' + str(
                cube[5][i + 2]) + '|')

    def move(self, action):
        if action in self.moves:
            self.moves[action]()
        else:
            print("'{0}'是不合法的输入".format(action))

    def move_edge(self, b, pa, sa=[0, 0, 0, 0]):
        # b: before;    pa: place after;    sa:status after;
        self.cube["EP"][b[0]], self.cube["EP"][b[1]], self.cube["EP"][b[2]], self.cube["EP"][b[3]] = \
            self.cube["EP"][pa[0]], self.cube["EP"][pa[1]], self.cube["EP"][pa[2]], self.cube["EP"][pa[3]]
        self.cube["ES"][b[0]], self.cube["ES"][b[1]], self.cube["ES"][b[2]], self.cube["ES"][b[3]] = \
            (self.cube["ES"][pa[0]] + sa[0]) % 2, (self.cube["ES"][pa[1]] + sa[1]) % 2, (self.cube["ES"][pa[2]] + sa[2]) % 2, (self.cube["ES"][pa[3]] + sa[3]) % 2

    def move_conner(self, b, pa, sa=[0, 0, 0, 0]):
        # b: before;    pa: place after;    sa:status after;
        self.cube["CP"][b[0]], self.cube["CP"][b[1]], self.cube["CP"][b[2]], self.cube["CP"][b[3]] = \
            self.cube["CP"][pa[0]], self.cube["CP"][pa[1]], self.cube["CP"][pa[2]], self.cube["CP"][pa[3]]
        self.cube["CS"][b[0]], self.cube["CS"][b[1]], self.cube["CS"][b[2]], self.cube["CS"][b[3]] = \
            (self.cube["CS"][pa[0]] + sa[0]) % 3, (self.cube["CS"][pa[1]] + sa[1]) % 3, (self.cube["CS"][pa[2]] + sa[2]) % 3, (self.cube["CS"][pa[3]] + sa[3]) % 3

    def moves_r(self):
        self.move_edge([3, 10, 7, 11], [11, 3, 10, 7])
        self.move_conner([3, 2, 6, 7], [7, 3, 2, 6], [2, 1, 2, 1])

    def moves_r2(self):
        self.move_edge([3, 10, 7, 11], [7, 11, 3, 10])
        self.move_conner([3, 2, 6, 7], [6, 7, 3, 2])

    def moves_r3(self):
        self.move_edge([3, 10, 7, 11], [10, 7, 11, 3])
        self.move_conner([3, 2, 6, 7], [2, 6, 7, 3], [2, 1, 2, 1])

    def moves_u(self):
        self.move_edge([0, 1, 2, 3], [3, 0, 1, 2])
        self.move_conner([0, 1, 2, 3], [3, 0, 1, 2])

    def moves_u2(self):
        self.move_edge([0, 1, 2, 3], [2, 3, 0, 1])
        self.move_conner([0, 1, 2, 3], [2, 3, 0, 1])

    def moves_u3(self):
        self.move_edge([0, 1, 2, 3], [1, 2, 3, 0])
        self.move_conner([0, 1, 2, 3], [1, 2, 3, 0])

    def moves_f(self):
        self.move_edge([0, 11, 4, 8], [8, 0, 11, 4], [1, 1, 1, 1])
        self.move_conner([0, 3, 7, 4], [4, 0, 3, 7], [2, 1, 2, 1])

    def moves_f2(self):
        self.move_edge([0, 11, 4, 8], [4, 8, 0, 11])
        self.move_conner([0, 3, 7, 4], [7, 4, 0, 3])

    def moves_f3(self):
        self.move_edge([0, 11, 4, 8], [11, 4, 8, 0], [1, 1, 1, 1])
        self.move_conner([0, 3, 7, 4], [3, 7, 4, 0], [2, 1, 2, 1])

    def moves_l(self):
        self.move_edge([1, 8, 5, 9], [9, 1, 8, 5])
        self.move_conner([0, 4, 5, 1], [1, 0, 4, 5], [1, 2, 1, 2])

    def moves_l2(self):
        self.move_edge([1, 8, 5, 9], [5, 9, 1, 8])
        self.move_conner([0, 4, 5, 1], [5, 1, 0, 4])

    def moves_l3(self):
        self.move_edge([1, 8, 5, 9], [8, 5, 9, 1])
        self.move_conner([0, 4, 5, 1], [4, 5, 1, 0], [1, 2, 1, 2])

    def moves_d(self):
        self.move_edge([4, 7, 6, 5], [5, 4, 7, 6])
        self.move_conner([4, 7, 6, 5], [5, 4, 7, 6])

    def moves_d2(self):
        self.move_edge([4, 7, 6, 5], [6, 5, 4, 7])
        self.move_conner([4, 7, 6, 5], [6, 5, 4, 7])

    def moves_d3(self):
        self.move_edge([4, 7, 6, 5], [7, 6, 5, 4])
        self.move_conner([4, 7, 6, 5], [7, 6, 5, 4])

    def moves_b(self):
        self.move_edge([2, 9, 6, 10], [10, 2, 9, 6], [1, 1, 1, 1])
        self.move_conner([2, 1, 5, 6], [6, 2, 1, 5], [2, 1, 2, 1])

    def moves_b2(self):
        self.move_edge([2, 9, 6, 10], [6, 10, 2, 9])
        self.move_conner([2, 1, 5, 6], [5, 6, 2, 1])

    def moves_b3(self):
        self.move_edge([2, 9, 6, 10], [9, 6, 10, 2], [1, 1, 1, 1])
        self.move_conner([2, 1, 5, 6], [1, 5, 6, 2], [2, 1, 2, 1])
