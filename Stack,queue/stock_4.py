from collections import deque
def solution(prices):
    answer = []
    tmp=0
    q = deque(prices)
    
    while q:
        cur_=q.popleft()
        #Think variable
        for i in q:
            tmp+=1
            if cur_ > i:
                if len(prices) == 0:
                    tmp=0
                
                break
        answer.append(tmp)
        tmp=0
                
    return answer

prices = [1, 2, 3, 2, 3]
#[4, 3, 1, 1, 0]

print(solution(prices))
