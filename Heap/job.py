import heapq

def solution(jobs):
        answer, now, i = 0,0,0
        start = -1
        heap = []

        while i < len(jobs):
            for j in jobs:
                print(start,j[0],now)
                if start < j[0] <= now:
                    heapq.heappush(heap, [j[1],j[0]])
                    #print(start,j[0],now)
            if len(heap) > 0:
                cur = heapq.heappop(heap)
                start = now
                now += cur[0]
                answer += now - cur[1]
                i+=1
            else:
                now += 1
        return answer // len(jobs)


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
