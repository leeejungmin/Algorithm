def solution(n, lost, reserve):
    answer = 0
    wear = [1 for _ in range(n+1)]
    #apply each case

    for j in lost:
        wear[j] = 0
    for k in reserve:
        wear[k] = 2
        
    print(wear)
    for i in range(1,n+1):
        #out of range when i+1, care about it
        if wear[i] == 0 and i<n:
            if wear[i+1] == 2 or wear[i-1] == 2:
                wear[i] += 1
                if wear[i+1] == 2:
                    wear[i+1] -= 1
                elif wear[i-1] == 2:
                    wear[i-1] -= 1
                # Think in detail.. about answer.. after treat, ignore or count
                answer+=1
        elif wear[i] == 0 and i==n:
            if wear[i-1] == 2:
                wear[i] += 1
                wear[i-1] -= 1
                answer+=1
        else:
            answer+=1
    print(wear)
    return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]

n=3
lost = [3]
reserve = [1]

print(solution(n, lost, reserve))
