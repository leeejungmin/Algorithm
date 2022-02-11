def solution(answers):
    answer = [0 for i in range(3)]
    #print([0]*3)
    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    dic={}
    
    dic[0]=man1
    dic[1]=man2
    dic[2]=man3

    print(dic)
    for i in range(len(answers)):
        ans = answers[i]
        print(man2[i%len(man1)])
        if(man1[i%len(man1)] == ans):
            answer[0] += 1
        if(man2[i%len(man2)] == ans):
            answer[1] += 1
        if(man3[i%len(man3)] == ans):
            answer[2] += 1     
    
    result = []
    for i in range(len(answer)):
        if(answer[i] == max(answer)):
            result.append(i+1)
    print(result)
    
    return sorted(result)

ans =[1,3,2,4,2]
#print(solution(ans))


def solutions(answers):
        score=[0]*3
        result=[]
        man1 = [1,2,3,4,5]
        man2 = [2,1,2,3,2,4,2,5]
        man3 = [3,3,1,1,2,2,4,4,5,5]
        dic={}
        
        dic[0]=man1
        dic[1]=man2
        dic[2]=man3
        print(dic)
        for i in range(3):
            for idx, ans in enumerate(answers):
                #print(i,idx,ans)
                if ans==dic[i][idx]:
                    score[i]+=1
                    
        

        for i in range(len(score)):
            if(score[i] == max(score)):
                result.append(i+1)
        return sorted(result)        
print(solutions(ans))
