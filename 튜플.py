def solution(s):
    s = s.split('},')
    str_nums = []
    for x in s:
        x = x.lstrip('{')
        x = x.rstrip('}')
        str_nums.append(x)
    str_nums.sort(key=lambda x: len(x))
    split_nums = []
    for num in str_nums:
        num = num.split(',')
        split_nums.append(num)
    answer = [int(split_nums[0][0])]
    for i in range(1, len(split_nums)):
        b = set(split_nums[i])
        a = set(split_nums[i-1])
        c = (b - a).pop()
        answer.append(int(c))
    return answer
