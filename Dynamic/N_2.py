def solution(N, number):
    answer = 0
    numbers= [[] for _ in range(1,9)]
    #loop 1~9, if 2 -> 55, 5+5 ,5-5,5*5,5/5
    for i in range(1,9):
        tmp=[]
        if i == 1:
            numbers[i] = [5]
            continue
        numbers[i].extend([int(i*str(N))])
        #3 -> 12 21
        #for matching each case .. how??? add another iterable logic 
        for j in range(i):
            for num1 in numbers[j]:
                #why not iterable? Should be array in 
                for num2 in numbers[i-j+1]:
                    tmp.extend([num1 + num2])
                    tmp.extend([num1 - num2])
                    tmp.extend([num1*num2])
                    if num2!=0:
                        tmp.extend([num1/num2])
            numbers[i].extend(tmp)
            if number in tmp:
                return i
                
    return answer

N = 5
number = 12
#4

print(solution(N, number))
