import heapq

def solution(operations):
    answer = []
    heap = []
    tmp = []
    for i in operations:
        if i == "D 1":
            #remove max
            heapq.heappop(tmp)
        elif i == "D -1":
            #remove min
            heapq.heappop(heap)
        else:
            split_ = i.split(" ")
            heapq.heappush(i[1])
        print(tmp)
    return answer

operations = ["I 16","D 1"]
##0
operations = ["I 7","I 5","I -5","D -1"]
##7,5
print(solution(operations))
