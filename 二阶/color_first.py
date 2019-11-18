from 二阶 import cube2
import time
import copy
import random

def slover_status():
    allow_moves = ["U", "U2", "U'", "R", "R2", "R'", "F", "F2", "F'"]
    step = 1
    res = []
    while step < 12:
        # print("于" + str(time.time() - start) + "s开始搜索" + str(step) + "步")
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
            if flag and moves[0] < 9 and moves[-1] < 9:
                path = []
                for move in range(len(moves)):
                    path.append(allow_moves[moves[move]])
                    test.one_move(allow_moves[moves[move]])
                if test.is_status_finish():
                    # test.show_cube()
                    res.append(path)
                else:
                    test.reset(c_place=copy.deepcopy(start_status[0]), c_status=copy.deepcopy(start_status[1]))
            moves[-1] += 1
            if len(res) > 10:
                return res
        step += 1

def slover_all():
    # test.show_cube()
    start_status = copy.deepcopy([test.c_place, test.c_status])
    allow_moves = ["U", "U2", "U'", "R2", "F2"]
    step = 1
    this_start = time.time()
    while step < 16:
        # print("于"+str(time.time() - start)+"s开始搜索"+str(step)+"步")
        moves = [0 for i in range(step)]
        while moves[0] < 5:
            if time.time() - this_start > 10:
                return False
            flag = True
            for i in range(step - 1, 0, -1):
                if moves[i] < 3 and moves[i - 1] < 3:
                    moves[i] = 2
                    flag = False
                    break
                elif moves[i] == moves[i-1]:
                    flag = False
                    break
                if moves[i] > 4:
                    moves[i] = 0
                    moves[i - 1] += 1
            if flag and moves[0] < 5 and moves[-1] < 5:
                path = []
                for move in range(len(moves)):
                    path.append(allow_moves[moves[move]])
                    test.one_move(allow_moves[moves[move]])
                if test.is_all_finish():
                    # test.show_cube()
                    return path
                else:
                    test.reset(c_place=copy.deepcopy(start_status[0]), c_status=copy.deepcopy(start_status[1]))
            moves[-1] += 1
        step += 1

test = cube2.cube()
# 二阶段搜索：参考色先法
times = []
while True:
    get_input = input('ENTRY MOVE(Q: reset):')
    start = time.time()
    moves = test.get_moves(get_input)
    for single_move in moves:
        test.one_move(single_move)
    test.show_cube()

    start_status = copy.deepcopy([test.c_place, test.c_status])
    res = slover_status()
    count = 0
    solvers = []
    for step1 in res:
        test.reset(c_place=copy.deepcopy(start_status[0]), c_status=copy.deepcopy(start_status[1]))
        for single_move in step1:
            test.one_move(single_move)
        res2 = slover_all()
        if res2:
            count += 1
            solvers.append(step1 + res2)
            # print(step1 + res2)
        else:
            solvers.append(step1 + ['超过10秒'])
            print('太久了放弃')

    for solver in solvers:
        print(solver)
    end = time.time()
    print(count)
    print("时间:" + str(end - start) + "s")
    times.append(end - start)
