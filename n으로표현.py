def solution(N, number):
    d = {i: set([int(str(N)*i)]) for i in range(1, 9)}
    step_cnt = 1
    while step_cnt < 9:
        for i in range(1, step_cnt):
            s1 = d[i]
            s2 = d[step_cnt-i]
            for x in s1:
                for y in s2:
                    d[step_cnt].add(x * y)
                    d[step_cnt].add(y * x)
                    if y > 0:
                        d[step_cnt].add(x // y)
                    if x > 0:
                        d[step_cnt].add(y // x)
                    d[step_cnt].add(x + y)
                    d[step_cnt].add(y + x)
                    d[step_cnt].add(x - y)
                    d[step_cnt].add(y - x)
        if number in d[step_cnt]:
            return step_cnt
        step_cnt += 1
    return -1


def solution(N, number):
    s = [set() for x in range(8)]
    for i, x in enumerate(s, start=1):
        x.add(int(str(N)*i))
    for i in range(1, len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 + op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
    return answer