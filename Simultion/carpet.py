def solution(yellow, brown):
    s = yellow + brown
    for i in range(s,2,-1):
        if s%i == 0:
            a = s//i
            if yellow == (a-2)*(i-2):
                return[i,a]
