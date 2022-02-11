from collections import defaultdict

def solution(tickets):
    # 1. 그래프 생성
    routes = dict()

    for (start, end) in tickets:
        routes[start] = [end]
        #routes[start] = routes.get(start, []) + [end]  
        print(routes, routes.get(start),routes.keys())
    # 2. 시작점 - [끝점] 역순으로 정렬    
    for r in routes.keys():
        routes[r].sort(reverse=True)

    print('routes',routes)
    # 3. DFS 알고리즘으로 path를 만들어줌.
    st = ["ICN"]
    path = []
    
    while st:
        top = st[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(st.pop())
            print('if not here',path,st)
        else:
            st.append(routes[top][-1])
            print('else here first', routes[top][-1], routes[top][:-1])
            routes[top] = routes[top][:-1]
            print('else here',st,routes[top])
    # 4. 만든 path를 거꾸로 돌림.
    answer = path[::-1]
    return answer

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))
        
