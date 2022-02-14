import heapq
def solution(operations):
    answer = []
    #2 kind of heap
    maxheap = []
    minheap = []
    for i in operations:
        
        a= i.split(" ")
        print(a)
        if a[0] == "I":
            a[1] = int(a[1])
            heapq.heappush(maxheap,(-a[1],a[1]))
            heapq.heappush(minheap,a[1])
        elif a[0] == "D":
            if a[1] == "1":
                #?
                max_ =heapq.heappop(maxheap)[1]
                minheap.remove(max_)
            else :
                min_ = heapq.heappop(minheap)
                maxheap.remove((-min_,min_))

    if maxheap:
        answer = [heapq.heappop(maxheap)[1],heapq.heappop(minheap)]
    else : answer = [0,0]
    return answer

operations = ["I 7","I 5","I -5","D -1"]
#[7,5]
print(solution(operations))
