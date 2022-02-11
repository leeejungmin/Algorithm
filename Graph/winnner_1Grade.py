def solution(n, results):
    answer = 0
    #win,lose configuration
    win=[[] for _ in range(n+1)]
    lose=[[] for _ in range(n+1)]
    for a,b in results:
        print(a,b)
 #       if a>b:
        win[a].append(b)
        lose[b].append(a)
##        else:
##            win[b].append(a)
##            lose[a].append(b)
    print(win,lose)
    #len(lose[i])+len(win[i]) == len(win)
    # for 5, 4312 , if lose 5,2 -> 2, 5431 -> 5 append 431 -> 4, 3-> 4
    for i in range(len(win)):
        for j in win[i]:
            for k in win[j]:
                if k not in win[i]:
                    #check for each 
                    print(k not in win[i],k,win[i])
                    win[i].extend([k])
            
    for i in range(len(lose)):
        for j in lose[i]:
            for k in lose[j]:
                if k not in lose[i]:
                    
                    lose[i].extend([k])
    print(win,lose)
    for i in range(len(win)):
        print(len(lose[i]),len(win[i]),len(win))
        if len(lose[i])+len(win[i]) == len(win)-2:
        #think logic of win length -1 = bef + aft + own 
            answer+=1
            #if i
            print(win,lose)
    return answer

# mapping for each case


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
##print(solution(n,results))
#a=results[0].extend([5,7])

#print(results)
##results[0].extend([3])
##print(results)

#2. use dic

from collections import defaultdict
def solutions(n, results):
    answer = 0
    win_graph = defaultdict(set)    # 이긴 애들
    lose_graph = defaultdict(set)   # 진 애들
    
    for winner,loser in results:        # 결과에서 이기고 진 애들 그래프화
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)
    
    for i in range(1,n+1):         
        for winner in win_graph[i]:                    # i한테 진 애들은 i를 이긴 애들한테도 진 것
            lose_graph[winner].update(lose_graph[i])
        for loser in lose_graph[i]:                     # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것
            win_graph[loser].update(win_graph[i])
    print(winner,loser)
    for i in range(1,n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:   # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
            answer += 1

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solutions(n,results))
