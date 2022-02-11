def solution(n, computers) :
    answer = 0
    global visited
    visited = [-1 for _ in range(3)]
    print(visited)
    global q
    q = [0]
    for i in range(n):
        print(i)
        if visited[i] == -1:            
            dfs(i)
            answer+=1
    return answer
def dfs(n):
    
    while q:
        pop=q.pop()
        print(computers[pop])
        for i in range(len(computers[pop])):
            if visited[i] == -1:
                if computers[n][i] == 1:
                    visited[i] = 1
                    q.append(i)
# 1 -> 2 , 3    
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	

print(solution(n,computers))
