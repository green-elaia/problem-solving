def solution(number, k):
    answer = []
    for i in range(k):
        answer.append(number[i])

    remaining_amount = k
    idx = k
    while remaining_amount:
        min_x = min(answer)
        if min_x <= number[idx]:
            cnt = answer.count(min_x)
            for _ in range(cnt):
                answer.remove(min_x)
                answer.append(number[idx])
                idx += 1
                remaining_amount -= 1
                if not remaining_amount:
                    break
        elif min_x > number[idx]:
            idx += 1
            remaining_amount -= 1

    answer = answer + list(number[idx:])
    return ''.join(answer)


if __name__ == '__main__':
    solution('4177252841', 4)