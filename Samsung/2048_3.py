vote = []

##Candi = [Candidate(name) for name in data]
###input = sys.stdin.readline()
##while len(Candi)>0:
##    c.score = [c[0] for i in votes].count(c.number)
##    for c in Candi:
##        minscore = min(c.score)
##    if minscore:
##        continue
   
n = 5
for i in range(n - 2, 0, -1):
    print(i)

def down(board):
    for j in range(n):
        for i in range(n):
            #point 0일때

            #다를때

            #같을때

def right(board):
    #point n-2, cur n-1, moving y
    pointer = n-2
    
    for i in range(n):
        for j in range(n-1,-1,-1):
            x = board[j][i]
            if board[pointer][i] == x:
                board[j][i] = 0
                board[pointer][i] = 2*x
                pointer -=1
            elif board[pointer][i] == 0:
                #다음로직을 더 정확하게 나눠야한다 즉, 볼수 있도록 작성..
                board[pointer][i] = x
                pointer -=1
            else:
                pointer -=1