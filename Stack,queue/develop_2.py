def solution(progresses,speeds):
    from collection import deque
    time = 0
    answer = []
    for i in range(len(progresses)):
        while progresses[i]+time*speeds[i] >= 100 
            time += 1
        answer.append(time)
    q = []
    cnt = 1
    for i in range(0,len(answer)-1):
        if answer[i]>answer[i+1]
            cnt += 1      
        else:
            cnt = 1
        q.append(cnt)
        # [7,3,9] -> [2,1]
