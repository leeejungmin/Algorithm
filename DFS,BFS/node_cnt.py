def solution(n,computers):
    answer = 0
    for i in range(n):
        if visited[i]==False:
            dfs(i,computers)
            answer+=1
            
def dfs(n,computers):
    visited = [[0] for i in range(n)]
    #for i in range(n):
     #   for j in range(n):
      #      visited[i] = 0
            
    while q:
        i = q.pop()
         for j in range(n)
            if computers[i][j] == 1 and visited[i] == False:
                q.append(j)
                visited[i] = True

