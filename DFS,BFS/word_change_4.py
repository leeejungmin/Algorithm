def solution(begin, target, words):
    answer = 0
    answer = candidate(begin,words,target)
    return answer

def candidate(word,words,target):
    #show list
    candi = [word]
    q=[[word,words,candi]]
    while q:
        word,words,candi = q.pop()
        print(word,words)
        if word == target:
            return len(candi) -1
        for i in words:
            cnt = 0
            #compare if 1 different
            for a,b in zip(word,i):
                if a!=b:
                    cnt+=1
                print(a,b,cnt)
            if cnt == 1:
                print('here')
                words.remove(i)
                candi.append(i)
                q.append([i,words,candi])
                
    #return candi

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin,target,words))
##print(candidate(word,words))
