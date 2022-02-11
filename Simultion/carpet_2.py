def solution(brown,yellow):
    carpet_s = brown + yellow
    for row in range(1,carpet_s): 
        col = carpet_s//row
        if (col-2)*(row-2) == yellow:
            return [col,row]

brown = 10
yellow = 2
print(solution(brown,yellow))
