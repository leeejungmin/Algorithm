import sys
input = sys.stdin.readline
# 4
# RRUU
n = int(input())
d = list(map(str,input().split()))
##d = input.split()
x,y = 1,1
#xy RLUD
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in d:
	if i == 'R':
		j = 0
	elif i == 'L':
		j = 1
	nx = x+dx[j]
	ny = y+dy[j]
	if 0<nx<=n and 0<ny<=n:
		x,y = nx,ny
	else:
		continue

print(x,y)
