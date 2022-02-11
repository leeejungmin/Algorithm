def solution(array, commands):
    answer = []
    temp = []
    #array[2,5] -> sort(array) -> array[k+1]->append
    for i in range(len(commands)):
        if commands[i][0] == commands[i][1]:
            temp = [array[commands[i][0]-1]]
        else:
            temp = array[commands[i][0]-1:commands[i][1]]
        
        print('first',temp)
        #temp = array[str(i[0]):str(i[1])]
        if len(temp)>1:
            temp_sorted = sorted(temp)
            print('second',commands[i][2],temp_sorted)
            answer.append(temp_sorted[commands[i][2]-1])
            print('third',answer)
        else :
            answer.append(temp)
            print('here if')
        #passport
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
#563
print(solution(array, commands))
for i in range(1,4):
    print(i)

#범위지정시 고려 x 
