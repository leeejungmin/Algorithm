def solution(triangle):
    for i in range(1,len(triangle)):
        #for j in range(i+1):
        for j in range(len(triangle[i])-1):
            if j==0:
                triangle[i][0] = triangle[i-1][0] + triangle[i][0]
            elif j==len(triangle[i]):
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            else :
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
                #understanding the problem
                #why I miss one ..
                #Miss range, review logic
                
    return max(triangle[len(triangle)-1])
    #return max(triangle[-1])
#triangle[-1]

triangle= [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
