def solution(gems):
    answer = []
    m_len = []
    m_list = set(gems)
    minimum = [[0]*100,1,1]
    #search every case
    #min length containing m_list
    for i in range(len(gems)):
        for j in range(i+1,len(gems)+1):
            #print(m_list,gems[i:j])
            if m_list == set(gems[i:j]):
                answer = gems[i:j]
                m_len.append([gems[i:j],i,j])
    print(m_len)
    for i in m_len:
        if len(minimum[0]) > len(i[0]):
            minimum = i
    answer = [minimum[1]+1,minimum[2]]
    return answer

##gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
#[3, 7]

gems = ["AA", "AB", "AC", "AA", "AC"]
#[1, 3]
print(solution(gems))
