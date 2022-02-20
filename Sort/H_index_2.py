def solution(citations):
    answer = 0
    #65301
    citations.sort(reverse=True)
    print(citations)
    for idx,val in enumerate(citations):
        #why? write detail by drilling down
        if val == (idx+1):
            return val

citations= [3, 0, 6, 1, 5]
#3
print(solution(citations))
