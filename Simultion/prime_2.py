def is_prime(n):
    if n < 2:
        False
    for i in range(2,n//2+1):
        if n%i == 0:
            return False

    return True

def solution(nums):
    answer = 0
    from itertools import combinations
    combi = combinations(nums,3)
    for a,b,c in combi:
        if is_prime(a+b+c):
            answer+=1
    return answer


nums=[1,2,3,4]
#nums=[1,2,7,6,4]
print(solution(nums))
