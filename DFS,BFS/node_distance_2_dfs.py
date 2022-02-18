def solution(n, computers) :
    answer = 0
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        if visited[i] == 0:
            stack = [i]
            dfs(stack, n, computers,visited)
            answer+=1
        print(i,answer)
    return answer

def dfs(stack, n, computers,visited):
    #0 -> 1, 2 
    while stack:
        cur_ = stack.pop()
        #print(cur_)
        for j in range(len(computers[cur_])):
            #if same as own 
            if j==cur_:
                visited[cur_] = 1
                continue
            
            if computers[cur_][j] == 1:
                if visited[j] == 0:
                    visited[j] == 1
                    stack.append(j)

    print(visited)
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#2
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))
