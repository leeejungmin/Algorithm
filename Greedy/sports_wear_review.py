def solution(n, lost, reserve):
    #same as set
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    print(_reserve,_lost)
    for r in _reserve:
        f = r - 1
        b = r + 1
        #for == ->if in
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

n = 5
lost = [2, 4]
reserve = [1, 3, 5]

#print(solution(n, lost, reserve))

reserve.remove(3)
print(reserve)
