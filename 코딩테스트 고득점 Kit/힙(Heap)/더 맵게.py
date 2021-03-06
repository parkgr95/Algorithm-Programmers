import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + 2 * heapq.heappop(scoville))
        except IndexError:
            return -1
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))