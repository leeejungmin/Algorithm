def solution(triangle):
    answer = 0
    #think range logic in detail
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            if j==0:
                triangle[i+1][j] += triangle[i][j]  
            elif j == len(triangle[i])-1:
                triangle[i+1][j+1] += triangle[i][j]
            else:
                triangle[i+1][j] += max(triangle[i][j-1],triangle[i][j])
   answer = max(triangle[-1])
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
#30
print(solution(triangle))
