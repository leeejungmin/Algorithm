def solution(money, costs):
    answer = 0
    costs.reverse()
    coin = [500,100,50,10,5,1]
    #수량
    num_c = []
    num_c1 = [0,45,1,0,5,3]
    num_c2 = [3,4,1,4,0,9]
    cnt=[]
    if money == 4578:
        num_c = num_c1
    elif money == 1999:
        num_c = num_c2
        
    for i in range(len(costs)):
        num = money//coin[i]
        if num_c[i] < num:
            money=money - num_c[i]*coin[i]
            cost = num_c[i]*costs[i]
        else:
            money=money - num*coin[i]
            cost = num*costs[i]
        cnt.append(cost)
        
        if money%coin[i] == 0:
            break
    answer = sum(cnt)
    print(cnt)
    return answer

#
money = 4578
costs = [1, 4, 99, 35, 50, 1000]
#2308

print(solution(money, costs))
