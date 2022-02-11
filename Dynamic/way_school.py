def solution(m,n,puddles):
    graph =[[1]*(m+1) for i in range(n+1)]
    
    
    for i in range(1,m):
        for j  in range(1,n):
            if [i,j] in puddles:
                print("here puddle")
                graph[i][j] = 0
            graph[i][j] = graph[i-1][j] + graph[i][j-1]
            
    return graph[m][n]
    #웅덩이가 2,2로 표현되어 있으니, 원래 좌표1,1인좌표에서 수정. 
    print(graph)
print(solution(4,3,[2,2]))
