def solution(n,computers):
    cnt = 0
    visited = [0 for i in range(n)]
    
    for i in range(n):
        if visited[i] == 0:
            dfs(n,i,computers,visited)
            cnt +=1

    return cnt

def dfs(n,k, computers,visited):

    visited[k] = True
    print(visited, k)
    for i in range(n):
        if computers[k][i] == 1 and visited[i] == 0 and k != i:
            dfs(n,i,computers,visited)
        else: continue

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
#computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))
