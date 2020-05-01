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



def solution(tickets):
    # 사전을 이용하여 각 공항에서 출발하는 항공권의 리스트를 표현하고 리스트는 역순으로 정렬. 그래야 시간 덜 걸림
    # 그래프를 구현하는 방식은 정방행렬을 이용한 인접행렬 방식과 연결리스트를 이용한 인접리스트 방식이 있음
    routes = {}   # 문제의 그래프를 딕셔너리로 구현(인접리스트 방식과 비슷)
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ['ICN']
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:  # 한붓그리기 특성 때문에 가능한 조건
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]
