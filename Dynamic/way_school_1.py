def solution(m, n, puddles):
    answer = 0
    #map, number of col,row
    map_=[[1]*(m+1) for _ in range(n+1)]
    
    print(map_)
    #puddle -> -1
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(map_)
            print(i,j)
            #logic
            if i == 1 or j == 1:
                map_[i][j] = 1
                
            else:
                map_[i][j] = map_[i][j-1] + map_[i-1][j]
                
            if i==puddles[0][0] and j==puddles[0][1]:
                map_[i][j]=0
    answer = map_[-1]
    return answer
#logic x,y in detail
# in iterating, misunderstand x,y position
m=4
n=3
puddles=[[2, 2]]
#4
print(puddles[0][0])
print(solution(m,n,puddles))
