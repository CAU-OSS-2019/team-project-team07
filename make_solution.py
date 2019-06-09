sol_table = [0] * 10


def check_solution(a='x', b='x', c='x', d='x'):
    result = '정상자 : '+str(a)+'\n'
    result += '제 1, 제 2 색각 이상자 : '+str(b)+'\n'
    result += '제 3 색각 이상자 : '+str(c)+'\n'
    result += '전색약, 전색맹 : '+str(d)+'\n'
    # print('정상자 : ', a)
    # print('제 1, 제 2 색각 이상자 : ', b)
    # print('제 3 색각 이상자 : ', c)
    # print('전색약, 전색맹 : ', d)
    return result


def power_solution(a='x', b='x', c='x', d='x', e='x', f='x', g='x'):
    result = '정상자 : '+str(a)+'\n'
    result += '제 1 (강도) : ' + str(b) + '\n'
    result += '제 2 (강도) : ' + str(c) + '\n'
    result += '제 1 (중등도) : ' + str(d) + '\n'
    result += '제 2 (중등도) : ' + str(e) + '\n'
    result += '제 1 (약도) : ' + str(f) + '\n'
    result += '제 2 (약도) : ' + str(g) + '\n'
    # print('정상자 : ', a)
    # print('제 1 (강도) : ', b)
    # print('제 2 (강도) : ', c)
    # print('제 1 (중등도) : ', d)
    # print('제 2 (중등도) : ', e)
    # print('제 1 (약도) : ', f)
    # print('제 2 (약도) : ', g)
    return result


def solution():

    target_num = sol_table[0]
    result = '제 '+str(target_num)+'표'+'\n'
    # print('제 ', target_num, '표')
    if target_num in [1]:
        result += check_solution(sol_table[1] + sol_table[2], sol_table[1] + sol_table[2], sol_table[1] + sol_table[2], sol_table[1] + sol_table[2])
    elif target_num in [2, 4]:
        result += check_solution(sol_table[1], sol_table[3], sol_table[1])
    elif target_num in [3, 5]:
        result += check_solution(sol_table[1]+sol_table[2], sol_table[3] + sol_table[4], sol_table[1] + sol_table[2])
    elif target_num in [6, 8]:
        result += check_solution(sol_table[1], 'x', sol_table[1])
    elif target_num in [7]:
        result += check_solution(sol_table[1] + sol_table[2], 'x', sol_table[1] + sol_table[2])
    elif target_num in [9]:
        result += check_solution('x', sol_table[1])
    elif target_num in [10]:
        result += check_solution(sol_table[1]+sol_table[2], sol_table[1]+sol_table[2])
    elif target_num in [11]:
        result += check_solution('긴 길', '지름길', '긴길')
    elif target_num in [12]:
        result += check_solution('o', 'x', 'o')
    elif target_num in [13, 14, 19]:
        result += power_solution(sol_table[1] + sol_table[2], sol_table[2], sol_table[1], sol_table[1] + sol_table[2], sol_table[1] + sol_table[2], sol_table[1] + sol_table[2], sol_table[1] + sol_table[2])
    elif target_num in [15, 16, 20]:
        result += power_solution(sol_table[1] + sol_table[2], 'x', 'x', sol_table[2], sol_table[1], sol_table[1] + sol_table[2], sol_table[1] + sol_table[2])
    elif target_num in [17, 18, 21]:
        result += power_solution(sol_table[1] + sol_table[2], 'x', 'x', 'x', 'x', sol_table[2], sol_table[1])

    return result
