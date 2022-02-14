from itertools import permutations
def solution(numbers):
    answer = 0
    per_num=[]
    print(permutations(numbers))
    #map
    for i in range(1,len(numbers)+1):
        tmp = set(list(map(int,map("".join,permutations(numbers,i)))))
        per_num.extend(tmp)
                       
    for num in per_num:
        if is_prime(num):
            answer+=1
    print(per_num)
    return answer

def is_prime(num):
    
    if num < 2:
        return False
    #Think cases of logic ex) 11%1 -> always 0
    for i in range(2,num//2+1):
        if num%i == 0:
            print(num%i,num,i)
            return False
        else:
            return True
numbers = "17"
#3
#numbers = "011"
#2
print(solution(numbers))
