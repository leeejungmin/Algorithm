from collections import deque
from itertools import permutations

def make_link(link):
    arr = []
    for idx, link in enumerate(link):
        for j in link:
           arr.append([idx,j])
    return arr

def is_link(n,link):
    for i in range(n):
        for j in range(len(link[i])):
            for k in range(len(link[j])):
                    if link[j][k] == i or link[j][k] in link[i]:
                        pass
                    else:                    
                        link[i].extend([link[j][k]])                       
    return len(make_link(link))
    
       
def solution(n, edges):
    answer = 0 
    link = [[] for _ in range(n)]
    visited=[[i] for i in range(n)]
    arr = []
    #match
    for i in edges:
        x = i[0]
        y = i[1]
        arr.append([x,y])
        arr.append([y,x])
        link[x].append(y)
        link[y].append(x)
    print()
    total = list(permutations(visited,2))
    answer = is_link(n,link)
    return answer
    

n=5
edges = [[0,1],[0,2],[1,3],[1,4]]
n=4
edges = [[2,3],[0,1],[1,2]]
print(solution(n, edges))
