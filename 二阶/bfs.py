from 二阶 import cube2
import time
import copy

def solver():
    allow_moves = ["U", "U2", "U'", "R", "R2", "R'", "F", "F2", "F'"]
    step = 1
    while step < 12:
        print("于" + str(time.time() - start) + "s开始搜索" + str(step) + "步")
        moves = [0 for i in range(step)]
        while moves[0] < 9:
            flag = True
            for i in range(step - 1, 0, -1):
                if moves[i] // 3 == moves[i - 1] // 3:
                    flag = False
                    break
                if moves[i] == 9:
                    moves[i] = 0
                    moves[i - 1] += 1
            # print(moves)
            if flag and moves[0] < 9 and moves[-1] < 9:
                path = []
                for move in range(len(moves)):
                    path.append(allow_moves[moves[move]])
                    test.one_move(allow_moves[moves[move]])
                if test.is_all_finish():
                    return path
                else:
                    test.reset(c_place=copy.deepcopy(start_status[0]), c_status=copy.deepcopy(start_status[1]))
            moves[-1] += 1
        step += 1

test = cube2.cube()

# 暴力广度优先搜索
times = []
while True:
    get_input = input('ENTRY MOVE(Q: reset):')
    start = time.time()
    moves = test.get_moves(get_input)
    for single_move in moves:
        test.one_move(single_move)
    test.show_cube()

    start_status = copy.deepcopy([test.c_place, test.c_status])
    print(solver())
    end = time.time()
    print("时间:" + str(end - start) + "s")
    times.append(end - start)
