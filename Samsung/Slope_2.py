import sys

input = sys.stdin.readline
n,l = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def solution(i,l,n,a)
    #각 열에 대에서
    height = 0
    for j in range(n):
        is_s = [0 for _ in range(n)]
        #detail,,, think every side - +
        if abs(a[i][j] - a[i+1][j]) > 1 : return False
        if a[i][j] - a[i+1][j] == 1:
            height = a[i+1][j] 
            if i+1+l > n: return False
            #check l is enough
            else:
                ##detail... think narrow position not decide just n....
                for k in range(i+1,i+1+l):
                    #check same len
                    if height != a[k]:
                        return False
                    ##think case
                    if not is_s[k]: return False
                        
                    is_s[k] = 1
            
    return True 
        #A[I] - A[I+1] = 1
            #길이가 I+1+L<N 
                #A[I] == A[I+1]
                #경사로 세웠는지