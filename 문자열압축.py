def solution(s):
    answer = len(s)
    for unit_len in range(1, len(s)):
        comp_str = []
        cnt = 0
        unit = s[:unit_len]
        remain_len = len(s)
        for j in range(0, len(s), unit_len):
            if s[j:j+unit_len] == unit:
                cnt += 1
            else:
                if cnt > 1:
                    comp_str.append(str(cnt))
                comp_str.append(unit)
                cnt = 1
                unit = s[j:j+unit_len]
            if remain_len >= unit_len:
                remain_len -= unit_len
        else:
            if cnt > 1:
                comp_str.append(str(cnt))
            if len(unit) == unit_len:
                comp_str.append(unit)
            if remain_len != 0:
                comp_str.append(s[-remain_len:])

        comp_str = ''.join(comp_str)
        if answer > len(comp_str):
            answer = len(comp_str)
    return answer
