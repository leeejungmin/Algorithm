from itertools import combinations

def is_prime(nums):
    if nums == 0 or nums == 1:
        return False
    
    for i in range(2,nums//2+1):
        if nums%i == 0:
            print('here')
            return False
        else:
            #print('true')
            answer = True
    return answer

def solution(nums):
    answer = 0
    arr = list(combinations(nums,3))
    print(arr)
    for ar in arr:
        print(ar)
        if is_prime(sum(ar)):
            answer+=1

    return answer


nums=[1,2,7,6,4]
#print(is_prime(5))
print(solution(nums))
