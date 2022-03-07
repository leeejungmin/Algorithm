from collections import deque
b = int(input())
#board
#board = [([0] for _ in range(b)) in range(n)]
board = [[0] * N for _ in range(N)]
n = int(input())
#apple = [list(map(int,input().split())) for _ in range(n)]
t = int(input())
order = [list(map(int,input().split())) for _ in range(t)]

#pos > 0,0 > length 1
#direction D -> right, L -> left

##logic of snake
#move(head,tail) -> if apple, del apple keep tail(x,y)
#if not apple, del tail (x,y), move head, tail(x+~,y+~)

