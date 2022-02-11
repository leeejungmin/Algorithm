def solution(numbers, target):
    global temp
    temp=[]
    global ans
    ans = 0
    #for idx, number enumerate(numbers):
    dfs(0,0)

    return ans
    #count -> ans
    #1 1 -> 2 0 -> 2
def dfs(sum_,idx):
    #idx = idx+1
    global ans
    
    if idx == len(numbers):
        if sum_==target:
            ans+=1
            temp.append(sum_)
    else:      
        #think the range of idx in array
        #idx until 4
        idx = idx+1
        dfs(sum_+numbers[idx-1],idx)
        dfs(sum_-numbers[idx-1],idx)
        
        #if use global var
    

#useless var input, make it effective


numbers = [1, 1, 1, 1, 1]
target = 3
#return 5

#nubmers = [4, 1, 2, 1]
#target = 4
#2
print(solution(numbers,target))
#why? time spend?? -> lack of logical(sum_,idx), need knowledge of var(global,nonlocal),
#idx counting, if else
#but I can solve finally. don't give up

