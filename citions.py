def solution(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        print(idx,citation)
        if idx >= citation:
            return idx


print(solution([3,0,1,6,5]))
