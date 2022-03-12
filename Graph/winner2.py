def solution(n, results):
    answer = 0
    winner = dict()
    loser = dict()
    winner_tmp = [[] for _ in range(n+1)]
    lose_tmp = [[] for _ in range(n+1)]
    #make graph of who win, lose
    for i in results:
        w,l = i[0],i[1] 
        winner_tmp[w].extend([l])
        lose_tmp[l].extend([w])
    print(winner_tmp,lose_tmp)
    #if lose 3, it is same as lose 4
    for i in range(1,n+1):
        #why??? not think carfully about list logic,for order
        #when change look after other logic effected
        for j in winner_tmp[i]:
            #print(j)
            if len(winner_tmp[i]) >= 1 :
                winner_tmp[i].extend(winner_tmp[j])
                
            else:
                pass
            #for k in j:
                #winner_tmp[i].extend([winner_tmp[j]])
        if len(winner_tmp[i]) >= 1:
            winner_tmp[i]=set(winner_tmp[i])
        for j in lose_tmp[i]:
            if len(lose_tmp[i]) >= 1:
                lose_tmp[i].extend(lose_tmp[j])
            else:
                pass
#            for k in j:
                #lose_tmp[i[0]].extend([lose_tmp[j]])
        if len(lose_tmp[i]) >=1:
            lose_tmp[i]=set(lose_tmp[i])
    for i in range(1,n+1):
        print(len(winner_tmp[i]),len(lose_tmp[i]))
        if n-1 == len(winner_tmp[i])+len(lose_tmp[i]):
            answer+=1
    #logic if len(win) == n-1 > cnt
    
    print(winner_tmp,lose_tmp)
    
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
#2
print(solution(n,results))
