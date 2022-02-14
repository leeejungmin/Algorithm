def solution(bridge_length, weight, truck_weights):
    answer = 0
    cnt = 0
    from collections import deque
    q = deque(weight)
    cur_ = deque(cur_)
    #iterate
    #logic  weight < 10
    while q:
        
        if sum(cur_) + next_ < 10
            cur_.append(next_)
        #when arrive, start 0 , but keep going previous one, 0->1->2,0->0->1->2 or 0->0->0->1->2
            next_ = q.popleft()
        #each truck -> 2s -> 1 2, 1 [2,1] 1
            
            cnt+=1
            if cnt == bridge_length:
                cur_.popleft()
        else:
            continue
         
        #time
        answer+=1
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))
#8
