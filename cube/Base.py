from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):

    def __init__(self):
        # todo 构造初始魔方
        self.cubeRules = {}

        self.cube = {}
        self.moves = {}

        self.init_cube()
        self.init_moves()
        pass

    # todo 初始化魔方
    @abstractmethod
    def init_cube(self):
        pass

    # todo 初始化合法的转动
    def init_moves(self):
        pass

    # 转动
    @abstractmethod
    def move(self, action):
        pass

    @abstractmethod
    def draw_cube(self):
        # todo 画出魔方当前的状态
        pass
