def solution(s,t):
    cnt = 0
    print(s.replace(t,""))
    while t in s: 
        s = s.replace(t,"")
        print("here",s)
        cnt+=1
    return cnt
    
s = "aabcbcd"
t = "abc"
print(solution(s,t))
