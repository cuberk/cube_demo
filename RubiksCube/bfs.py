from RubiksCube import cube3
import time
import copy

def slover():

    moves = test.get_moves(get_input)
    for single_move in moves:
        test.one_move(single_move)
    test.show_cube()

    # 一阶段：20步之内调整色向
    print([test.e_place, test.e_status, test.c_place, test.c_status])
    start_status = copy.deepcopy([test.e_place, test.e_status, test.c_place, test.c_status])
    allow_moves = ["U", "U2", "U'", "R", "R2", "R'", "L", "L2", "L'", "F", "F2", "F'", "B", "B2", "B'", "D", "D2", "D'"]

    step = 1
    count1 = 0
    count2 = 0
    while step < 12:
        moves = [0 for i in range(step)]
        while moves[0] < 18:
            count2 += 1
            flag = True
            for i in range(step - 1, 0, -1):
                if moves[i] // 3 == moves[i - 1] // 3:
                    flag = False
                    break
                if moves[i] == 18:
                    moves[i] = 0
                    moves[i - 1] += 1
            if flag and moves[0] < 18 and moves[-1] < 18:
                count1 += 1
                path = []
                for move in range(len(moves)):
                    path.append(allow_moves[moves[move]])
                    test.one_move(allow_moves[moves[move]])
                if test.is_status_finish():
                    test.show_cube()
                    return path
                else:
                    test.reset(e_place=copy.deepcopy(start_status[0]), e_status=copy.deepcopy(start_status[1]), c_place=copy.deepcopy(start_status[2]), c_status=copy.deepcopy(start_status[3]))
            moves[-1] += 1
        step += 1
    print("查找条数: " + str(count2))
    print("有效条数: " + str(count1))


test = cube3.cube()
# 打乱
get_input = input('ENTRY MOVE(Q: reset):')
start = time.time()
print(slover())
end = time.time()
print("时间:" + str(end - start) + "s")

