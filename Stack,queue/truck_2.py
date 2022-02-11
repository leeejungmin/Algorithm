def solution(bridge_length, weight, truck_weights):
    from collections import deque
    truck_weights = deque(truck_weights)
    answer = 0
    temp_weight = []
    cnt=0
    #7->7 -> 4 ->45->5->6->6->0
    while truck_weights:
        #cur_truck = truck_weights.pop()
        #print('truck',cur_truck)
        
        print('truck_weight',truck_weights)
        #while  if < 10,cnt -> 1 2 1 2 2 1 2 
        
        if weight > sum(temp_weight)+(truck_weights[0]):
            temp_weight.append(truck_weights.popleft())
            print('temp',temp_weight,sum(temp_weight[:]))
            print('cnt',cnt)
            
        if cnt == bridge_length:
            temp_weight.pop()
            cnt = 0
            print('-----')
        
        cnt += 1              
        answer += 1
    return answer

truck_weights = [7,4,5,6]
bridge_length = 2
weight = 10

print(solution(bridge_length, weight, truck_weights))
