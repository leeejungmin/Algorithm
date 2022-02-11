def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            print('이')
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            print(progresses,speeds,count)
            
        else:
            print('일')
            print(progresses,speeds,count,time,answer)
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

ans = [93, 30, 55]
spd = [1, 30, 5]
print(solution(ans,spd))

