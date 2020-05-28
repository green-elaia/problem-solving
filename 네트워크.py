def solution(n, computers):
    answer = 0
    visited_node = [False] * n
    stack = []

    for root_idx, v in enumerate(visited_node):
        if not v:
            stack.append(root_idx)
            while len(stack) != 0:
                i = stack[-1]
                if not visited_node[i]:
                    visited_node[i] = True
                for j, j_val in enumerate(computers[i]):
                    if i != j and j_val == 1 and not visited_node[j]:
                        stack.append(j)
                        break
                else:
                    stack.pop()
            answer += 1
    return answer
