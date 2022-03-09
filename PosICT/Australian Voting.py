s1=input()
s1=int(s1)
name=[]
for i in range(s1):
    naming=input()
    name.append(naming)


cnt=[0,0,0]
vote=[[1,2,3],[2,1,3],[2,3,1],[1,3,2],[3,1,2]]
per50=round((len(vote)+0.1)/2)

for i in range(len(vote)):
    j=0
    if vote[i][j]== 1:
        cnt[0]=cnt[0]+1
    elif vote[i][j]== 2:
        cnt[1]=cnt[1]+1
    elif vote[i][j]== 3:
        cnt[2]=cnt[2]+1
maxcnt=0
mincnt=0
for i in range(len(cnt)):
    if cnt[i]>cnt[maxcnt]:
        maxcnt=i
    if cnt[i]<cnt[mincnt]:
        mincnt=i

    if cnt[maxcnt]<per50:
        for i in range(len(vote)):
            j=0
            if vote[i][j]==cnt[mincnt]:
                for i in range(len(vote)):
                    j=1
                    if vote[i][j]== 1:
                        cnt[0]=cnt[0]+1
                    elif vote[i][j]== 2:
                        cnt[1]=cnt[1]+1
                    elif vote[i][j]== 3:
                        cnt[2]=cnt[2]+1
print("max",name[maxcnt])
