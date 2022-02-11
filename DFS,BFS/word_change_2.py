from itertools import permutations
    
def solution(begin, target, words):
    answer = 0
    
    queue=[begin]
    cnt=0
    #begin(hot)->dot->lot...
    while words:
        q = words.pop()
        #print(q)
        next_=list(q)
        for i in next_:
            q.append(i)
        #print(next_)
        
        cnt+=1
        if next_ == target:
            answer=cnt
            return answer
        
                
    return answer

#should process under here like dfs
from collections import deque
def list(cur_):
    cnt=0
    temp =[]
    #check funtional event
    cur_q = deque([cur_])
    while cur_q:
        visited = [-1 for _ in range(len(words))]
        for i in range(len(words)):
            for a,b in zip(cur_q,words[i]):
                if a!=b:
                    cnt+=1
            if cnt == 1:
                if visited[i] == -1:
                    temp.append(words[i])
                    q.append([words[i],i])
                    visited[i] = 1
                    #words.pop(i)
                    
        cnt = 0
        print(cur_,temp)
    return temp
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
words.remove("dog")
print(words)
#print(list("dog"))
#print(solution(begin,target,words))
#a = list(permutations(begin,3))
#temp=[]
#return 4
#for i in a:
#    print(temp.append("".join(i)))
#    print(temp)
#print(list(permutations(begin,3)))
#print(solution(begin,target,words))

#for a,b in zip(begin,target):
#    print(a,b,a==b)
