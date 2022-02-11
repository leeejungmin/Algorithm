def solution(prices):
    
    from collections import deque

    q = deque(prices)
    time = 0
    answer = []
    
    while len(q):
        item = q.popleft()
        time = 0
        for i in q:
            
            print(item,i,q,time)
            if item>i:
                #answer.append(time)
                time = 1
                if len(prices)==1:
                    time=0
                break
            else:
                time+=1
        answer.append(time)
    
    return answer

ans=[1, 2, 3, 2, 3]
print(solution(ans))

