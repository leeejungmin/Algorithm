from collections import deque
def solution(n, vertex):
    answer = 0
    #make graph
    from collections import defaultdict
    
    
    #v = defaultdict()
    v = [[] for _ in range(n+1)]
    for a,b in vertex:
        v[a].extend([b])
        v[b].extend([a])
    print(v)
    #bfs from 1 -> [v,dis]
    visited = bfs(v)
    for i in visited:
        if max(visited) == i:
            answer +=1
    
    return answer
def bfs(v):
    #when change, consider other conditions
    visited = [-1 for _ in range(n+1)]
    q = deque([[1,0]])
    #iterate
    while q:
        #deque logic
        cur_,dep = q.popleft()
        print(cur_,dep)
        #1 ->2 3 -> 4 -> 3
        #understading problem -> visited check once done
        
        for next_ in v[cur_]:
            #visited check
            print(next_,visited)
            if visited[next_] == -1:
                visited[next_] = dep+1
                #logic of append
                q.append([next_,dep+1])
                #logic of var
    return visited        
    
    

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,vertex))
##return 3

##city = ('Chongqing', 'China', 30165500)
##print(city[-1])
