def solution(comple,parti):
    dic=dict()
    for i in range(parti):
        dic[hash(i)] = i
        sum_pe += hash(i)
    for j in range(comple):
        dic[hash(j)] = j
        sum_pe += hash(j)

    return dic[sum_pe]
