from itertools import combinations as c

n = int(input())
array = [i for i in range(n)]
matrix = []
for _ in range(n):
    matrix.append((list(map(int, input().split()))))
result = int(1e9)
for r1 in c(array, n//2):
    start, link = 0, 0
    r2 = list(set(array) - set(r1))
    for r in c(r1, 2):
        start += matrix[r[0]][r[1]]
        start += matrix[r[1]][r[0]]
    for r in c(r2, 2):
        link += matrix[r[0]][r[1]]
        link += matrix[r[1]][r[0]]
    result = min(result, abs(start-link))
print(result)

#########################

import sys

input = sys.stdin.readline

def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    start += a[i][j]
                elif not select[i] and not select[j]:
                    link += a[i][j]
        ans = min(ans, abs(start - link))

    for i in range(idx, n):
        if select[i]:
            continue
        select[i] = 1
        dfs(i + 1, cnt + 1)
        select[i] = 0


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

select = [0 for _ in range(n)]
ans = sys.maxsize
dfs(0, 0)
print(ans)