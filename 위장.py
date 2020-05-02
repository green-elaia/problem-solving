def solution(clothes):
    d = dict()
    for x in clothes:
        d[x[1]] = d.get(x[1], []) + [x[0]]
    answer = 1
    for k in d:
        answer *= len(d[k]) + 1
    return answer - 1