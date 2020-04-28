def solution(scoville, k):
    import heapq as h
    h.heapify(scoville)  # O(nlog_n)
    cnt = 0
    while scoville:
        a = h.heappop(scoville)
        if a < k and scoville:
            b = h.heappop(scoville)
            new = a + b*2
            h.heappush(scoville, new)  # O(log_n)
            cnt += 1
        elif a >= k:
            break
        else:
            cnt = -1
    return cnt



def solution(scoville, k):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= k:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        new = min1 + min2*2
        heapq.heappush(scoville, new)
        answer += 1
    return answer