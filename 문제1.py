def solution(numbers, hand):
    pos = [(4,2), (1,1), (1,2), (1,3), (2,1), (2,2), (2,3),(3,1), (3,2), (3,3)]
    pos_L, pos_R = (4,1), (4,3)

    answer = []
    for num in numbers:
        if num in [1,4,7]:
            answer.append('L')
            pos_L = pos[num]
        elif num in [3,6,9]:
            answer.append('R')
            pos_R = pos[num]
        else:
            d_L = abs(pos[num][0] - pos_L[0]) + abs(pos[num][1] - pos_L[1])
            d_R = abs(pos[num][0] - pos_R[0]) + abs(pos[num][1] - pos_R[1])
            if d_L < d_R:
                answer.append('L')
                pos_L = pos[num]
            elif d_L > d_R:
                answer.append('R')
                pos_R = pos[num]
            else:
                if hand == 'left':
                    answer.append('L')
                    pos_L = pos[num]
                elif hand == 'right':
                    answer.append('R')
                    pos_R = pos[num]

    return ''.join(answer)