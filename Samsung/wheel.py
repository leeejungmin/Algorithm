from collections import deque
import sys

input = sys.stdin.readline
wheel = deque([[] for I in  range(4)])
queue = []
for j in range(4):
    a = list(input().split())

    for i in a:
        wheel[j].extend(i)
    b = deque(wheel[j])
    queue.append(b)
n = int(input())
order = [[] for I in range(n)]
for i in range(n):
    a = map(int,input().split()) 
    for j in a: 
        order[i].append(j)

print(order,type(wheel[1][1]))
def rotation(i,direct):
    if (i+1)%2 == 0:
            direct = -direct
    else:
        direct = direct
        
    wheel[0].rotate(direct)
    wheel[1].rotate(-direct)
    wheel[2].rotate(direct)
    wheel[3].rotate(-direct)
    for j in range(3):
        if wheel[j][2] == wheel[j+1][6]:
                if (j+1)%2 == 0:
                    wheel[j+1].rotate(-direct)
                else:
                    wheel[j+1].rotate(direct)


for i in order:
    rotation(int(i[0]),int(i[1]))

print(wheel)
