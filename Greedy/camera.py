from collections import deque
def solution(routes):
    answer = 4
    routes.sort()
    #routes = deque(routes)
    #-13 >= -15 >= -18 -> is possible -> +1
    while routes:
        cur_ = routes.pop(0)[1]
        for route in routes:
            
            if route[0] <= cur_ <=route[1]:
                print(route[0],cur_,route[1])
                answer-=1
                routes.pop(0)
            else:
                continue
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
#2

print(solution(routes))
#why popleft iteration impossible?
