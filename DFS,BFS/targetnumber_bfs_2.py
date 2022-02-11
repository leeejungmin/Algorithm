def solution(numbers, target):
    ans = 0
    from collections import deque
    
    queue = [[numbers[0],1],[-numbers[0],1]]
    queue = deque(queue)
    while queue:
        sum_,idx=queue.popleft()
        if idx == len(numbers):
            if sum_==target:
                ans+=1
                print('here',sum_,idx)
            
        else:
            #print('here',sum_,idx)
            queue.append([sum_+numbers[idx],idx+1])
            queue.append([sum_-numbers[idx],idx+1])
    return ans

numbers = [4, 1, 2, 1]
#numbers = [1, 1, 1, 1, 1]
target = 4
print(solution(numbers,target))
#think every var whenever change something
