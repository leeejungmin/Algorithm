def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])
    print(d)

    while d:
        item = d.popleft()
        if max(d)[0] > item[0]:
            d.append(item)
            print(d)
        else:
            answer += 1
            print('answer',answer)
            if item[1] == location:
                break
    return answer

priorities = [2, 1, 3, 2]
location = 3
print(solution(priorities, location))
