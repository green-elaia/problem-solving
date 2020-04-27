def solution(number, k):
    stack = [number[0]]
    idx = 1
    str_size = len(number)
    while k and idx < str_size:
        if stack[-1] < number[idx]:
            stack.pop()
            k -= 1
            if not stack:
                stack.append(number[idx])
                idx += 1
        else:
            stack.append(number[idx])
            idx += 1
    while idx < str_size:
        stack.append(number[idx])
        idx += 1
    for _ in range(k):
        stack.pop()
    return ''.join(stack)



def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    return answer
