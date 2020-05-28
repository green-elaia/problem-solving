def solution(gems):
    s = set(gems)
    s_len = len(s)
    g_len = len(gems)
    for l in range(s_len, g_len+1):
        for i in range(g_len - l + 1):
            tmp = set(gems[i:i+l])
            if len(s - tmp) == 0:
                return [i+1, i+l]



def solution(gems):
    s = set(gems)
    s_len = len(s)
    a = []
    d = {}
    for i in range(len(gems)):
        if gems[i] not in d:
            d[gems[i]] = i
        else:
            d[gems[i]] = i
        if len(d) == s_len:
            tmp = []
            for v in d.values():
                tmp.append(v)
            else:
                tmp.sort()
            a.append([tmp[0]+1, tmp[-1]+1])

    a.sort(key=lambda x: x[1]-x[0])
    return a[0]

