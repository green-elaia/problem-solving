from collections import Counter
def solution1(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    for k in p:
        if c[k] is None or p[k] != c[k]:
            return k


def solution2(participant, completion):
    answer = dict()
    for k in participant:
        if k not in answer:
            answer[k] = 1
        else:
            answer[k] += 1
    for k in completion:
        answer[k] -= 1
    for k in answer:
        if answer[k]:
            return k


def solution3(participant, completion): # O(n)
    answer = dict()
    for k in participant:
        answer[k] = answer.get(k, 0) + 1
    for k in completion:
        answer[k] -= 1
    for k in answer:
        if answer[k]:
            return k
    # dnf = [k for k, v in d.items() if v > 0]
    # return dnf[0]


# 빠르기: solution2 > solution3 (get메소드와 리스트 컴프리핸션 때문인듯) > solution1 (import 시간 때문인듯)
# 파이썬에서 딕셔너리는 내부적으로 해시로 구현되고 키를 이용하면 O(1)시간으로 접근 가능
