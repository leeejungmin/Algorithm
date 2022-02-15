def solution(citations):
    answer = 0
    a = citations.sort(reverse=True)
    for idx, num in enumerate(citations):
        if (idx+1) == num:
            answer = num
    return answer

citations= [3, 0, 6, 1, 5]
#3
print(solution(citations))
