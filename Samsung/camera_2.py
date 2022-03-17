import sys

input = sys.stdin.readline
n,m = input().split(" ")
map_ = [list(map(int, input().split(" "))) for _ in range(n)]
cctv = []
ans = n*m

#동서남북
dy = [0,0,1,-1]
dx = [1,-1,0,0]

#find cctv
for i in range(n):
	for j in range(m):
		if map_[i][j] not in [0,6]:
			cctv.append([i,j,map_[i][j]])

show(map_,0)
#put cctv

def solution(cctv,dep,map_):
	res = 0
	if dep == len(cctv):
		res = map_.count(0)
	ans = min(ans,res)
	return ans
		


			show()
#choose camera type
def show(map_,dep):
	ans = solution(cctv,dep,map_)
	x,y,k = cctv[dep]
	if k = 1:
		for i in range(4):
			go(x,y,i,map_)
			show(map_,dep+1)
	elif k = 2:
		for i in [0,2]:
			go(x,y,i,map_)
			go(x,y,i+1,map_)
			show(map_,dep+1)
	elif k = 3:
		for i in range(4):
			go(x,y,i,map_)
			go(x,y,(i+2)%4,map_)
			show(map_,dep+1)
	elif k = 4:
		for i in range(4):
			go(x,y,i,map_)
			go(x,y,(i+1)%4,map_)
			go(x,y,(i+2)%4,map_)
			show(map_,dep+1)	
	elif k = 5:
			i=0
			go(x,y,i,map_)
			go(x,y,i+1,map_)
			go(x,y,i+2,map_)			
			go(x,y,i+3,map_)
			show(map_,dep+1)

	return ans
#fill as direction
def go(x,y,i):
	new = [map_[i][:]] for i in range(n)
	ny = y + dy[i]
	nx = x + dx[i]
	while 0 <= ny < n or 0 <= nx < m or new[ny][nx] != 6:
		if new[ny][nx] == 0:
			new[ny][nx] = '#'
		ny += dy[i]
		nx += dx[i]