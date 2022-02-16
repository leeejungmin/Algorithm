from collections import deque
def solution(numbers, target):
    answer = 0
    #logic of deque, list
    sums_ = deque([[-numbers[0],1],[numbers[0],1]])
    #sums_=[[-numbers[0],1],[numbers[0],1]]
    #1,-1 -> 1+1 1-1 -1+1 -1-1 -> ..
    while sums_:
        sum_,dep = sums_.popleft()
        if dep == len(numbers):
            print('here',sum_,dep)
            if sum_ == target:
                
                answer+=1
            continue
##        if dep == len(numbers)+1:
##            print(dep,len(numbers))
##            break
        #sum_=sum_+cur_, sum+-cur_
        #why? should finish above .. 
        cur_=numbers[dep]
        
        sums_.append([sum_+cur_,dep+1])
        sums_.append([sum_-cur_,dep+1])

    
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
#5
numbers = [4, 1, 2, 1]
target = 4
#2
print(solution(numbers, target))
