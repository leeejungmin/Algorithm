def solution(n, edge):
    answer = 0
    #graph
    #dfs
    return dfs(graph,n,edge)
    
def dfs(graph,n,edge):
    #stack [cur_,dep]
    stack = [[1,0]]
    #from 1 -> count 6 -> range(n+1)
    visited=[-1 for _ in range(n+1)]
    while stack:
        #1 -> 3,2 -> 5,4
        #visited 1 2 5
        cur_,dep = stack.pop()
        
        for next_ in graph[cur_]:
            if visited[next_] == -1:
                visited[next_]= dep+1
                stack.append([next_,dep+1])
        #check
            for i in visited:
                if max(visited) == i:
                    answer += 1
                    
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
#3

print(solution(n, edge))
