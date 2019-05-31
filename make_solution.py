sol_table = [0] * 10


def check_solution_print(a='x', b='x', c='x', d='x'):
    print('정상자 : ', a)
    print('제 1, 제 2 색각 이상자 : ', b)
    print('제 3 색각 이상자 : ', c)
    print('전색약, 전색맹 : ', d)


def power_solution_print(a='x', b='x', c='x', d='x', e='x', f='x', g='x'):
    print('정상자 : ', a)
    print('제 1 (강도) : ', b)
    print('제 2 (강도) : ', c)
    print('제 1 (중등도) : ', d)
    print('제 2 (중등도) : ', e)
    print('제 1 (약도) : ', f)
    print('제 2 (약도) : ', g)


def solution():
    target_num = sol_table[0]
    print('제 ', target_num, '표')
    if target_num in [1]:
        check_solution_print(sol_table[1] + sol_table[2], sol_table[1] + sol_table[2], sol_table[1] + sol_table[2], sol_table[1] + sol_table[2])
    elif target_num in [2, 4]:
        check_solution_print(sol_table[1], sol_table[3], sol_table[1])
    elif target_num in [3, 5]:
        check_solution_print(sol_table[1]+sol_table[2], sol_table[3] + sol_table[4], sol_table[1] + sol_table[2])
    elif target_num in [6, 8]:
        check_solution_print(sol_table[1], 'x', sol_table[1])
    elif target_num in [7]:
        check_solution_print(sol_table[1] + sol_table[2], 'x', sol_table[1] + sol_table[2])
    elif target_num in [9]:
        check_solution_print('x', sol_table[1])
    elif target_num in [10]:
        check_solution_print(sol_table[1]+sol_table[2], sol_table[1]+sol_table[2])
    elif target_num in [11]:
        check_solution_print('긴 길', '지름길', '긴길')
    elif target_num in [12]:
        check_solution_print('o', 'x', 'o')
    elif target_num in [13, 14, 19]:
        power_solution_print(sol_table[1] + sol_table[2], sol_table[2], sol_table[1], sol_table[1] + sol_table[2], sol_table[1] + sol_table[2], sol_table[1] + sol_table[2], sol_table[1] + sol_table[2])
    elif target_num in [15, 16, 20]:
        power_solution_print(sol_table[1] + sol_table[2], 'x', 'x', sol_table[2], sol_table[1], sol_table[1] + sol_table[2], sol_table[1] + sol_table[2])
    elif target_num in [17, 18, 21]:
        power_solution_print(sol_table[1] + sol_table[2], 'x', 'x', 'x', 'x', sol_table[2], sol_table[1])
