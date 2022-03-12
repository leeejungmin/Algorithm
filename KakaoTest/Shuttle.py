#m_bus = n*m
#time set (for i in range(n)) n 1 > 9+t*[i-1],
#number_p > i*m
#n-=1 > If nm < time = len(timtable) - nm l : answer = timtable[m] -1
#else : if time < m: answer 9 + n*t
def solution(n, t, m, timetable):
    answer = ''
    # timetable을 int형 분 단위로 전환하였음
    new_timetable = []
    for i, time in enumerate(timetable):
        new_timetable.append( int(time[0:2])*60 + int(time[3:]) )
    new_timetable.sort(reverse = True)
    
    # bus 시간 테이블을 만들었음(int형 분 단위로)
    bus_table = [540+(i*t) for i in range(n)]
    tmp_answer = 0
    bus_idx = 0
    # 처음 버스 부터 마지막 버스 까지 움직인다.
    while bus_idx < len(bus_table):
    	# 현재의 버스라고 가정함.
        stack = []
        bus_onboard = 0
        # 해당하는 버스에 정원이 다 찰때까지 인원을 세줌 
        while bus_onboard != m:
        	# 조건에 맞다면 인원을 버스에 태워준다.
            if len(new_timetable) >= 1 and new_timetable[len(new_timetable)-1] <= bus_table[bus_idx]:
                bus_onboard += 1
                # 버스에 탄다
                stack.append(new_timetable.pop())
            else:
                break
        # 만약 마지막 버스인데,
        if bus_idx == len(bus_table)-1:
        	# 정원이 다 찼다면
            if bus_onboard == m:
            	# 마지막으로 탄 한 명을 잡아댕겨서 빼주고 탈 준비.
                # 나는 무조건 같은 시간대 마지막으로 타기 때문에, 마지막 사람 - 1 을 해줘야함.
                tmp_answer = stack.pop() - 1
            # 정원이 다 안찼다면
            else:
            	# 천천히 갈 수 있으므로 최대한 늦게(버스 시간에 맞춰서)
                tmp_answer = bus_table[bus_idx]
        
        bus_idx += 1
    
    # int형 분단위를 string형 답으로 변환함.
    if tmp_answer//60 < 10:
        answer += '0'+str(tmp_answer//60)
    else:
        answer += str(tmp_answer//60)
    answer += ":"
    if tmp_answer%60 < 10:
        answer += '0'+str(tmp_answer%60)
    else:
        answer += str(tmp_answer%60)
    
    return answer

n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
print(solution(n, t, m, timetable))
