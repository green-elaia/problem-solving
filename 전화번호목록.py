def solution(phone_book):
    answer = True
    d = dict()
    for i, x in enumerate(phone_book):
        l = len(x)
        tmp = [k[:l] for k in phone_book][i+1:]
        if x in tmp:
            d[x] = d.get(x, 0) + 1
    for x in d:
        if d[x]:
            answer = False
    return answer



def solution(phone_book):
    answer = True
    hash_map = {}  # 접두어를 키로 갖는 딕셔너리
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
