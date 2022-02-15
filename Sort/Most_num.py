def solution(numbers):
    answer = ''
    cmp_num=dict()
    cmp_num2=[]
    tmp=[]
    tmp2=[]
    for idx, num in enumerate(numbers):
        
        num_multi = 3*str(num)
        #print(num,num_multi)
        cmp_num[num_multi] = idx 
    for key in cmp_num.keys():
        cmp_num2.append(key)
        
    cmp_num2 = sorted(cmp_num2,reverse=True)
    for i in cmp_num2:
        # 1234 idx
        tmp.append(cmp_num[i])
        # 6485 idx -> value -> arrange
    
    for j in tmp:
        tmp2.append(numbers[j])
        #back to origin num -> arrange
    tmp2=list(map(str,tmp2))
    print(tmp2)
    answer = "".join(tmp2)
    return answer

numbers = [6, 10, 2]
#"6210"
numbers = [3, 30, 34, 5, 9]
#"9534330"
print(solution(numbers))
