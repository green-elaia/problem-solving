def solution(genres, plays):
    d = dict()
    sum_d = dict()
    answer = list()
    for i in range(len(genres)):
        d[genres[i]] = d.get(genres[i], []) + [(i, plays[i])]
    for k in d:
        d[k].sort(key=lambda x: x[1], reverse=True)
        sum_d[k] = sum([x[1] for x in d[k]])
    sum_d = sorted(sum_d.items(), key=lambda x: x[1], reverse=True)
    for k, _ in sum_d:
        if len(d[k]) >= 2:
            answer.append(d[k][0][0])
            answer.append(d[k][1][0])
        else:
            answer.append(d[k][0][0])
    return answer
