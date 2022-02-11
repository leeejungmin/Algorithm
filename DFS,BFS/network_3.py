def solution(n,computers):
    answer = 0
    visited=[[0]*n]
    for i in range(n):
        if visited[i] == False:
            dfs(n,computers)
            answer+=1

    
def dfs(n,computers):
    q = [0]
    while q:
        next_ = q.pop()
        for i in range(len(computers[next_])):
            if visited[i] == False and computers[next_][i]:
                visited[i] = True
                q.append(i)
