def solution(board):
    st, co = 0, 0
    s = [[0,0,0]]
    while s[-1][0] < len(board) or s[-1][1] < len(board):
        if s[-1][1]+1 <= len(board) and board[s[-1][0]][s[-1][1]+1] == 0:
            if s[-1][2] == 0:
                st += 1
            elif s[-1][2] == 1:
                co += 1
            s.append([s[-1][0], s[-1][1] + 1, 0])
            continue
        elif s[-1][0]+1 <= len(board) and board[s[-1][0]+1][s[-1][1]] == 0:
            if s[-1][2] == 0:
                co += 1
            elif s[-1][2] == 1:
                st += 1
            s.append([s[-1][0], s[-1][1] + 1, 0])
            continue
        s.pop()
    return st * 100 + co * 500