from TwoByTwo import cube2
import time
import random

test = cube2.cube()
times = []

while True:
    get_input = input('ENTRY MOVE(Q: reset):')
    start = time.time()
    count = 0
    allow_moves = ["U", "U2", "U'", "R", "R2", "R'", "F", "F2", "F'"]
    moves = test.get_moves(get_input)
    for single_move in moves:
        test.one_move(single_move)
    while test.is_all_finish() == False:
        test.one_move(random.choice(allow_moves))
        count += 1
        if count % 100000 == 0:
            print(count)
            test.show_cube()
    print('次数:', count)
    print('时间:', time.time()-start)
    test.show_cube()