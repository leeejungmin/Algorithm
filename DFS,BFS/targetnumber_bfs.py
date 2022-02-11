def solution(numbers, target):
    from collections import deque
    ans = 0
    idx = 0
    q = deque([[1,1]])
    #1(1)->1+1,1-1(2)->
    while q:
        sum_,idx = q.popleft()
        idx +=1
        if  idx<len(numbers):
            q.append([sum_+numbers[idx],idx])
            q.append([sum_-numbers[idx],idx])
        else:
            if  sum_ == target:
                ans+=1
    return ans

numbers = [1, 1, 1, 1, 1]
target = 3
#return 5

print(solution(numbers,target))

if row*col == 
