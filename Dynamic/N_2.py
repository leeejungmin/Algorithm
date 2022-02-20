def solution(N, number):
    answer = 0
    numbers= [[] for _ in range(1,9)]
    #loop 1~9, if 2 -> 55, 5+5 ,5-5,5*5,5/5
    for i in range(1,9):
        if i == 1:
            numbers[i] == 5
            continue
        numbers[i].extend(int(i*str(N)))
        #3 -> 12 21
        #for matching each case .. how???
        for j in range(1,i):
            for k in range(i-j+1):
                numbers[i].extend(numbers[j] + numbers[k])
                numbers[i].extend(numbers[j] - numbers[k])
                numbers[i].extend(numbers[j] * numbers[k])
                if numbers[k]!=0:
                    numbers[i].extend(numbers[j] / numbers[k])
    for numbers
    return answer

N = 5
number = 12
#4

print(solution(N, number))
