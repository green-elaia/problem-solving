def solution(progresses, speeds):
    import math

    answer = []
    days = []
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))

    i = 0
    while i < len(days) - 1:
        if days[0] < days[i + 1]:
            answer.append(i + 1)
            days = days[i + 1 :]
            i = 0
        else:
            i += 1
    else:
        answer.append(i + 1)

    return answer
