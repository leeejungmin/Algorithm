def solution(participant, completion):
    answer = ''
    temp = 0
    dic={}
    for i in participant:
        dic[hash(i)] = i
        temp += hash(i)
    for j in completion:
        temp -= hash(j)
    print(dic)
    answer = dic[temp]
    return answer
    #collections.Counter(participant) - collections.Counter(completion)
    print(hash("leo"))
    return answer
#understanding hash
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant,completion))

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    temp = []
    q = participant
    while q:
        par =q.pop()
        for com in completion:
            if com != par:
                temp.append(par)
                
            elif com == par:
                completion.pop()
    return temp

#print(solution(participant,completion))

def solution(participant, completion):
    #part_dic = dict(participant)
    for idx, name in enumerate(participant):
        print(idx, name)
    print(part_dic)
print(solution(participant,completion))
