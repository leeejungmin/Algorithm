import sys
input = sys.stdin.readline
m,n,x,y,k = input().split()

map_d = [[map(int,input().split())] for _ in range(int(m))]
print(map_d)
