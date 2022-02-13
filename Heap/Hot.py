import heapq
def solution(scoville, K):
    answer = 0
    next_ = 0
    heapq.heapify(scoville)
    #c = a + b*2
    #heapq.pop(0),heapq.pop(1)
    
    while True:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        next_=a + b*2
        print(a,b,next_)
        answer+=1
        if next_ > K:
          break
        else:
            heapq.heappush(scoville,next_)
    

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))
