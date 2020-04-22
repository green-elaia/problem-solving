def solution1(n, lost, reserve):  # 0.04ms
    workout_clothes_num = [1 for i in range(n+2)]  # [1] * (n+2)
    for e in lost:
        workout_clothes_num[e] -= 1
    for e in reserve:
        workout_clothes_num[e] += 1
    for i, v in enumerate(workout_clothes_num):
        if v == 2:
            if workout_clothes_num[i-1] == 0:
                workout_clothes_num[i-1] += 1  # workout_clothes_num[i-1:i+1] = [1,1]
                workout_clothes_num[i] -= 1
            elif workout_clothes_num[i+1] == 0:
                workout_clothes_num[i+1] += 1
                workout_clothes_num[i] -= 1
    return n - workout_clothes_num.count(0)  # len([x for x in workout_clothes_num[1:-1] if x > 0])


# 만약 n이 엄청 크지만 reserve가 작다면?? array 사용이 비효율적임
# set() 사용 가능, set은 내부적으로 해시테이블로 구현되어 있음. 그래서 키 접근, 삽입이 O(1)임
def solution2(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l)
