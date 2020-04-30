def solution(tickets):
    visited = []  # stack
    tickets.sort(key=lambda x: x[1])
    used_ticket = {tuple(x) : 0 for x in tickets}
    visited.append('ICN')
    while True:
        check = 1
        dest = ''
        for v in used_ticket.values():
            check *= v
        if check == 1:
            break
        for k in used_ticket:
            if k[0] == visited[-1] and used_ticket[k] != 1 and k[1] != dest:
                visited.append(k[1])
                used_ticket[k] = 1
                break
        else:
            dest = visited.pop()
            used_ticket[[visited[-1], dest]] = 0
    return visited
