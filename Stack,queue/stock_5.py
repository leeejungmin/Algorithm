def solution(prices):
    answer = []
    
    from collections import deque
    prices = deque(prices)
    while prices:
        cnt=0
        cur_ = prices.popleft()
        for i in prices:
            if cur_<= i:
                cnt+=1
            else:
                if cnt == 0:
                    cnt+=1
                    
                if len(prices) == 0:
                    cnt = 0
                break
        answer.append(cnt)
        
    return answer

prices = [1, 2, 3, 2, 3]
#[4, 3, 1, 1, 0]
print(solution(prices))
