def solution(begin, target, words):
     dfs(begin)
def dfs(cur_):
    # if difference 1
    # visited check for each dfs
    visited=[-1 for _ in range(len(words))]
    q=[[begin,0,visited]]
    #visited[0] = 1 remove when I put temporary
    if target not in words:
        print('over---------------------')
        return 0
    temp =[]
    #for
    while q:
        print(q)
        word,dep,visited = q.pop()
        if word == target:
            
            temp.append(dep)
            print('---------------',temp)
            continue
        
        
        for i in range(len(words)):
            cnt = 0
            for a,b in zip(word,words[i]):
                #when change, consider var
                print(a,b)
                
                if a!=b:
                    cnt+=1
            print(cnt)
            if cnt == 1:
                print('here',visited[i])
                if visited[i] == -1 :
                    print('second')
                    visited[i] = 1
                    q.append([words[i],dep+1,visited])
    #when put var, think it what it is, not without think
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin,target,words))
