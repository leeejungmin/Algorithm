from itertools import combinations

def solution(n, costs):
    answer = 0
    tmp = []
    #how imply this logic?
##    lef,rig = 0,n
##    while lef>=n:
##        if is_connect(costs):
##            lef +=1
    #permutations and combinations
    candi = combinations(costs,3)
    for i in candi:
   if is_connect(i):
           sum_=i[0][2]+i[1][2]+i[2][2]
           tmp.append(sum_)
           answer = min(tmp)
##           print(i,tmp)
    return answer

def is_connect(cost):
    visited=[0 for _ in range(n)]
    tmp = []
    dis = 0
    for a,b,c in cost:
        
        if visited[a] == 0:
            visited[a] = 1
        if visited[b] == 0:
            visited[b] = 1
        dis+=1
    if 0 in visited:
        return False
    else:
        return True
        
        
    tmp = set(tmp)
    
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 4
#4
print(solution(n, costs))
