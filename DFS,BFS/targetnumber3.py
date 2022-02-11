def solution(numbers,target):
    answer = 0
    answer = DFS(numbers,target,0)
    return answer

def DFS(numbers,target,dep):
    answer = 0
    
    
    if dep == len(numbers):
        if sum(numbers) == target:
            return 1
        else return 0
    else:
        answer += DFS(numbers, target, dep+1)
        numbers[dep]*=-1
        answer += DFS(numbers, target, dep+1)

    return answer
