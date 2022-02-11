def solution(numbers, target):
    global temp
    temp=[]
    #global ans
    ans=0
    #for idx, number enumerate(numbers):
    dfs(1,1)

    return ans
    #count -> ans
def dfs(sum_,idx):
    idx = idx+1
    
    if idx <=len(numbers):
        print(sum_,idx)
        #think the range of idx in array 
        dfs(sum_+numbers[idx-1],idx)
        dfs(sum_-numbers[idx-1],idx)
        if idx == 5 and sum_ == target:
            temp.append(sum_)
            ans += 1
            print(temp,idx)
        #if use global var





numbers = [1, 1, 1, 1, 1]
target = 3
#return 5

#nubmers = [4, 1, 2, 1]
#target = 4
#2

print(solution(numbers,target))
