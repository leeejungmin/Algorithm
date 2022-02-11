from collections import deque

def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])
    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            #print(visited,v,count)
            for e in adj[v]:
                q.append([e, count])

def solution(n, edge):
    answer = 0
    visited = [-1] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
        print(x,y,adj[x],adj[y])
        #print(e,visited,adj)
        
    bfs(1, visited, adj)
    
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer


n = 5
edge = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n,edge))
