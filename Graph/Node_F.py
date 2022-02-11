from collections import deque

def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])
    while q:
        value = q.popleft()
        seq = value[0]
        count = value[1]

        if visited[seq] == -1:
            visited[seq] = count
            count += 1
            for e in adj[seq]:
                q.append([e,count])

def solution(n,edge):
    answer = 0
    visited = [-1]*(n+1)
    print(visited)
    adj = [[] for _ in range(n+1)]
    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
    bfs(1,visited,adj)
    print(visited)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer

edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6

print(solution(n,edge))
