def solution(user_id, banned_id):
    # 길이가 매우 짧으니까 O(n^3)도 괜춘
    sanction = []   # 제재아이디
    for b_id in banned_id:
        tmp = []
        for u_id in user_id:
            if len(b_id) == len(u_id):
                for i in range(len(b_id)):
                    if b_id[i] != '*' and b_id[i] != u_id[i]:
                        break
                else:
                    tmp.append(u_id)
        sanction.append(tmp)

    from itertools import product
    id_combination = list(product(*sanction))
    answer = len(id_combination)
    for x in id_combination:
        if len(set(x)) != len(banned_id):
            answer -= 1

    from math import factorial
    d = {}
    for x in banned_id:
        d[x] = d.get(x, 0) + 1
    for x in d:
        if d[x] > 1:
            answer = answer // factorial(d[x])

    return answer
