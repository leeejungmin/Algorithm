def solution(prices_s):
    #4 -> 3 -> 1-> 1 -> 0
    answer = []
    q = [prices_s[0]]
    #prices_s = []
    #for i in prices:
     #   prices_s.append(i)
    #prices_s.sort()
    #prices_s.insert(1,'good')
    #prices_s.pop()
    print(q,prices_s)
    tm = 1
    while prices_s:
        q = prices_s.pop()
        print(q)
        
        for i in range(len(prices_s)):
            if q <= prices_s[i]:
                tm +=1
                print(q,prices_s[i],tm)
            else:
                tm = 1
                #answer.append(tm)
                if len(prices_s)==0:
                    tm = 0
        answer.append(tm)
    return answer

prices_s = [1, 2, 3, 2, 3]
print(solution(prices_s))
#[4, 3, 1, 1, 0]
