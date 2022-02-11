def prime(ans):
    if ans < 2:
        return False
    for i in range(2,ans//2+1):
        if ans % i == 0:
            return False

    return True

def solution(nums):
    from itertools import permutations
    #from itertools import combinations
    combi = []
    for i in range(1,len(nums)+1):
        combi.extend( permutations(nums,i))
    answer = 0
    #print("".join(combi))

    a = set(list(map(int,map("".join,combi))))
    print(a)
    for i in a:
        print(i)
        if prime(i):
            print('here')
            answer+=1

    return answer
nums="17"
#3
#nums="011"
#2
print(solution(nums))

#col*row = brown + yellow
#(col-2)(row-2)=brown+yellow
