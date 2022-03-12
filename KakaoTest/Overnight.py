def solution(n, works):
    answer = 0
    #sort reverse, work[0] - 1, n-1
    #while n>0
    while n>0:
        works.sort()
        works[2] = works[2] - 1
        n-=1
        #print(works)
    #result
    answer = list(map(lambda x: x ** 2, works))
  
    return sum(answer)

works = [4, 3, 3]
n = 4
#12

##works = [2, 1, 2]
##n = 1
#6

print(solution(n, works))
