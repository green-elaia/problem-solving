def solution(board, moves):
    answer = 0
    stack = []
    new_board = {}
    board = board[::-1]
    for items in board:
        for i, item in enumerate(items):
            if item != 0:
                new_board[i] = new_board.get(i, []) + [item]

    for i in moves:
        if len(new_board[i-1]) != 0:
            x = new_board[i-1].pop()
        else:
            continue
        if len(stack) != 0 and stack[-1] == x:
            stack.pop()
            answer += 2
        else:
            stack.append(x)
    return answer
