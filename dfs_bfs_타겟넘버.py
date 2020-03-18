def solution1(number, target):
    end = 2**len(number)
    leaf = [0 for _ in range(end)]

    depth = 1
    last_depth = len(number)
    while depth <= last_depth:
        gap_cnt = 2**depth
        gap = end // gap_cnt
        idx = 0
        for i in range(gap_cnt):
            if not i % 2:
                for j in range(idx, idx+gap):
                    leaf[j] += number[depth-1]
            else:
                for j in range(idx, idx+gap):
                    leaf[j] -= number[depth-1]
            idx += gap
        depth += 1

    answer = leaf.count(target)
    return answer



def solution2(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution2(numbers[1:], target-numbers[0]) \
               + solution2(numbers[1:], target+numbers[0])