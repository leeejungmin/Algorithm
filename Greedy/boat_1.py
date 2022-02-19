def solution(people,limit):
    boat = []
    cnt=len(people)
    people.sort()
    while people:
        if sum(boat)+people[0]<=limit:
            cur_=people.pop()
            boat.append(cur_)
            if len(boat)>1:
                cnt-=1
                print(boat)
                boat=[]
        else:
            boat.pop()
        print(boat)
    return cnt

people = [70, 50, 80, 50]
limit = 100
print(solution(people,limit))
