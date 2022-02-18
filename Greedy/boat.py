def solution(people,limit):
    boat = []
    people.sort()
    cnt = len(people)
    visited = [0 for _ in range(cnt)]
    # if > 100
    for i in range(cnt):
        for j in range(cnt):
            #logic ->  describe it
            if visited[j] == 0:
                if i==j:
                    continue
                else:
                    if people[i] + people[j] <= limit:
                        print(people[i],people[j],i,j)
                        cnt-=1
        visited[i] = 1

    return cnt

people = [70, 50, 80, 50]
limit = 100
print(solution(people,limit))
            
        
                
            
