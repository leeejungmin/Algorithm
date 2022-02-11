def solution(N,number):
#5
#55, (5+5), (5-5), (5/5),(5*5)
#555,5 + 55, 5+5+5, 5
    G = [set([int(str(N)*i)]) for i in range(1,9)]
    #Need to know Set set([])...
    #print(G[0].add(5))
    print(G)
    #55..
    for i in range(1,9):
        temp=[]
        #3 -> 0.3 -> 1,2 -> 2,1 -> 3.0
        for j in range(i): 
            for x in G[j]:
                for y in G[i-j-1]:
                #1,0 -> G[0] -> G[2-0-1]
                #Detail in probelm -> solve myself    
                #why scope problem?
                    G[i].add(x+y)
                    G[i].add(x-y)
                    if x!=0:
                        G[i].add(y//x)
        for k in G[i]:
            print(G)
            if k == number:
                return i+1
        
    return -1

N = 3
number = 6

print(int(str(N)*2))
print(solution(N,number))
#something change, look after all algorithm
