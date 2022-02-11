def solution(prices):
    answer = []
    from collections import deque

    q = deque(prices)
    

    while len(q)>0:
        item=q.popleft()
        count = 0
        
        for i in q:
            count+=1
            print(item,q)
            if item>i:
                 break                        
        answer.append(count)
       
                
    return answer

ans=[1, 2, 3, 2, 3]
print(solution(ans))
