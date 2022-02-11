def solution(n,edge):

#Graph -> x -> y, y -> x
    global visited
    visited = [-1]*(n+1)
    graph = [[] for i in range(n+1)]
    dis = 0
    for i in edge:
        
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        print(i[0],i[1],graph,visited)
#all global variable?
        
    bfs(1,graph,dis)
    print(visited)
    return max(visited)  

def bfs(v,graph,dis):
    
    visited[v] = dis
    dis += 1
    for j in graph[v]:
        if visited[j] ==-1 :
            print('here',graph[j],visited)
            bfs(j,graph,dis)
#3,6???
#dis(from 1) 1 -> 2 -> 3
#max(visited)
#while or for, recursion
#v v[1] ->2,3 v[2]->5,6
n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
print(solution(n,edge))
