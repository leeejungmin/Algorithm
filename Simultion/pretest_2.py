def solution(answers):
    cnt = 0
    answer = []
    patter_1 = [ 1, 2, 3, 4, 5]
    patter_2 = [ 2, 1, 2, 3, 2, 4, 2, 5]
    patter_3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    pattern = dict()
    pattern[0] = patter_1
    pattern[1] = patter_2
    pattern[2] = patter_3

    pattern_2 = dict()
    print(pattern)
    
    for a,b in zip(patter_1,answers):
        if a==b:
            cnt +=1
            
    pattern_2[1] = cnt

    cnt = 0
    for a,b in zip(patter_2,answers):
        if a==b:
            cnt +=1
            
    pattern_2[2] = cnt

    cnt = 0
    for a,b in zip(patter_3,answers):
        if a==b:
            cnt +=1
            
    pattern_2[3] = cnt
    print(pattern_2)
    idx = 0
    for key,val in pattern_2.items():
 #       idx += 1
        
        #print(val, max(pattern_2))
        if val == max(pattern_2.values()):
            answer.append(key)

    return answer

answers = [1,2,3,4,5]
#[1]

answers = [1,3,2,4,2]
#[1,2,3]

print(solution(answers))
