def solution(expression):
    expr_list = []
    op = set()
    tmp = []
    for c in expression:
        if c in ['-', '+', '*']:
            expr_list.append(int(''.join(tmp)))
            expr_list.append(c)
            op.add(c)
            tmp = []
        else:
            tmp.append(c)
    else:
        expr_list.append(int(''.join(tmp)))

    answer = 0
    if len(op) == 1:
        tmp = 0
        if list(op)[0] == '+':
            for i in range(0, len(expr_list), 2):
                tmp += expr_list[i]
        elif list(op)[0] == '-':
            for i in range(0, len(expr_list), 2):
                tmp -= expr_list[i]
        elif list(op)[0] == '*':
            for i in range(0, len(expr_list), 2):
                tmp *= expr_list[i]
        if answer < abs(tmp):
            answer = tmp

    elif len(op) == 2:
        op = list(op)
        cal = [0,0]
        for j in range(2):
            tmp = expr_list
            for i in range(2):
                op1 = op[i+j-1]
                for _ in range(tmp.count(op1)):
                    idx = tmp.index(op1)
                    if op1 == '+':
                        tmp[idx-1] = tmp[idx-1] + tmp[idx+1]
                        del tmp[idx:idx+2]
                    elif op1 == '-':
                        tmp[idx - 1] = tmp[idx - 1] - tmp[idx + 1]
                        del tmp[idx:idx + 2]
                    elif op1 == '*':
                        tmp[idx - 1] = tmp[idx - 1] * tmp[idx + 1]
                        del tmp[idx:idx + 2]
            cal[j] = abs(tmp[0])
        cal.sort()
        if answer < cal[-1]:
            answer = cal[-1]

    elif len(op) == 3:
        op = [['+', '-', '*'], ['+', '*', '-']]
        cal = [[0, 0, 0], [0, 0, 0]]

        for k in range(2):
            op_list = op[k]
            for j in range(3):
                tmp = expr_list
                for i in range(3):
                    op1 = op_list[i+j-2]
                    for _ in range(tmp.count(op1)):
                        idx = tmp.index(op1)
                        if op1 == '+':
                            tmp[idx - 1] = tmp[idx - 1] + tmp[idx + 1]
                            del tmp[idx:idx + 2]
                        elif op1 == '-':
                            tmp[idx - 1] = tmp[idx - 1] - tmp[idx + 1]
                            del tmp[idx:idx + 2]
                        elif op1 == '*':
                            tmp[idx - 1] = tmp[idx - 1] * tmp[idx + 1]
                            del tmp[idx:idx + 2]
                cal[k][j] = abs(tmp[0])
            cal[k].sort()
        if cal[0][-1] > cal[1][-1]:
            r = cal[0][-1]
        else:
            r = cal[1][-1]
        if answer < r:
            answer = r

    return answer
