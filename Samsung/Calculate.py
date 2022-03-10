import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)

def dfss(sum,visited,n):
    for i in range(sum(a.values)):
        #dfs,visited check
        for j in range(len(visited)):
            if visited[j]:
                if j == 0:
                    sum[i]+=num[j]
                elif j == 1:
                    sum[i]-=num[j]
                elif j == 2:
                    sum[i]*=num[j]
                elif j == 3:
                    if num[j] != 0:
                        sum[i]/=num[j]
                visited[j]-=1
                dfs(sum,visited,dep,n)

#permutation
def permutations()
    for i in num:
        global max, min
        for j in sym:
            j == '+':
                sum+=i
            j == '-'
                sum-=i 

            sum = max(sum)