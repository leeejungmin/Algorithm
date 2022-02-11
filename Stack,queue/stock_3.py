def solution(prices):
    #4->3->1->1->0
    from collections import deque
    answer = []
    cnt = 0
    prices = deque(prices)
    
    while prices:
        q = prices.popleft()
        for i in range(len(prices)):
            if q <= prices[i]:
                cnt +=1
            else:
                cnt=1
                if len(prices) == 0:
                    cnt = 0
                break
        answer.append(cnt)
        cnt = 0
    return answer

prices= [1, 2, 3, 2, 3]
print(solution(prices))
#not consider condition in detail.
#1.not falling means including equal
#2.if falling, stop -> break
