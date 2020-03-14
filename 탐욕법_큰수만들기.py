def solution1(number, k):
    answer = []
    sorted_num = sorted(number, reverse=True)
    number = list(number)
    if number == sorted_num:
        return ''.join(number[:-k])
    i = 0
    while True:
        x = sorted_num[i]
        if x in number:
            idx = number.index(x)
            if idx <= k:
                answer.append(x)
                del number[:idx+1]
                k -= idx
                if not k:
                    break
                sorted_num.remove(x)
                i = 0
            else:
                i += 1
    
    answer = answer + number
    answer = ''.join(answer)
    return answer



def solution2(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)