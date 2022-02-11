def solution(money):
    #1번을 할경우, 마지막은 포함 안됨
    h1[0] = money[0]
    for i in range(len(money)-1):
        h1[i] = max(h1[i-1],h1[i-2]+money[i])
    #1번을 안할경우, 마지막 포함됨
    h2[0] = 0
    for i in range(len(money)):
        h2[i] = max(h2[i-1],h2[i-2]+money[i])

    return max(h1[len(money)-1],h2[len(money)])

    #식에 대한이해 부족
    #조건에 대한 디테일 부족

