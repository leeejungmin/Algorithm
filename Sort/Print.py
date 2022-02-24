def solution(priorities, location):
    answer = 0
    from collections import deque
    prioirites = [(b,a) for a,b in enumerate(priorities)]
    q = deque(prioirites)
    while True:
        cur_= q.popleft()
        if cur_[0] < max(q)[0]:
            print('here')
            q.append(cur_)
        else:
            print('heeee',q)
            q.insert(0,cur_)
            for idx, a in enumerate(q):
                print('++++',q)
                if a[1] == location:
                    
                    answer = idx+1
                    return answer
    

priorities = [2, 1, 3, 2]
location = 2
#1
##priorities = [1, 1, 9, 1, 1, 1]
##location = 0
#5
print(solution(priorities, location))
