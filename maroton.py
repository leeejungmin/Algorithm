def solution(participant, completion):
    #answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        #print(hash(part))
        #print(dic)
        temp += int(hash(part))
        temp += hash(part)

        print("dic",dic)
        print(temp)
    for com in completion:
        dic.pop(hash(com))
        #temp -= hash(com)
        print("com",hash(com))
        print(2,temp)
    #answer = dic[temp]
    for value in dic.values():
            answer = value
    print("dic",dic)
    return answer

par=["leo", "kiki", "eden"]
com=["eden", "kiki"]

print(solution(par,com))

