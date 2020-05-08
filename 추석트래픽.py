def solution(lines):
    time = []
    for line in lines:
        s, ms = line.split()[1:]
        s = float(s.split(':')[2])
        ms = float(ms[:-1])
        if len(time) != 0 and time[-1][0] >= 59.0 and s >= 0.0:
            s += 60.0
        time.append((s, round(s+ms, 3)))

    answer = 0
    t1 = time[0][0]
    t2 = round(t1 + 1.0, 3)
    while t1 <= time[-1][1]:
        cnt = 0
        for x in time:
            if x[1] <= t1 or x[0] >= t2:
                continue
            cnt += 1
        if cnt > answer:
            answer = cnt
        t1 = round(t1 + 0.001, 3)
        t2 = round(t1 + 1.0, 3)
    return answer
