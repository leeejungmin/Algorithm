def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: answer[i[1]] += 1
        else: answer[i[1]] = 1

    cnt = 1
    print(answer)
    for i in answer.values():
        
        cnt *= (i+1)
    return cnt - 1

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))

def solution(clothes):
    answer={}
    for cloth in clothes:
        if cloth[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] =1
    cnt=1
    for i in answer.value:
        cnt*=(i+1)

    return cnt-1

def solution(clothes):
    answer ={}
    for i in range(clothes):
        if i[1] in answer :
            answer[i[1]] +=1
        else:
            answer[i[1]] =1

    cnt = 1

    for i in answer.value():
        cnt *= (i+1)

    return cnt -1

def soltion(clothes):
    answer ={}
    for i in range clolthes:
        if i[1] in answer:
                answer[i[1]] +=1
        else: answer = 1

    cnt = 1

    for i in answer.value:
        cnt *= (i+1)

    return cnt -1



        
