
from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0, 0])
    V = [ 0 for i in range(len(words))]
    while q:
        word, cnt , n= q.popleft()
        if word == target:
            answer = cnt
            break        
        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append([words[i], cnt+1,i])
                    V[i] = 1
                    print(q,V)
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin,target,words))
