answer = 0

def solution(ans,target):
    global answer
    temp = 0
    root = 0

    
    check(ans, temp, root)
    
def check(ans, temp, root):
    global answer
    from collections import deque 
    ans = deque(ans)
    N=len(ans)
    #while ans :
    print(answer,target, temp)
         
     #   fir=ans.popleft()
    if temp == target:
            answer += 1
            print('here')
    else:       
        check(ans, temp + ans[root], root + 1)
        check(ans, temp - ans[root], root + 1)

        
    
    
    return answer

ans = [1, 1, 1, 1, 1]
target = 3

print(solution(ans,target))
