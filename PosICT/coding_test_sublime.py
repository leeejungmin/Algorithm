def solution(n,name,rating):
    cnt=0
    name_n=dict()
    rate = [0 for _ in range(n+1)]
    rate_d = dict()
    queue = []
    for n,idx in enumerate(name):
        name_n[n] = idx
        
    for i in rating:
        
        a = rate[i[0]]
        print(a,rate)
        rate[i[0]] = a + 1

    for r,idx in enumerate(rate):
        rate_d[r] = idx
    rate.sorted()
    print(rate)    
    
        if max(rate) > (len(rating)/2):
            for i in rate:
                candi.append(name[rate[0]])
                return candi
             
        else:
            for j,idx in enumerate(rating):
                if j[0] == rate[n]:
                    queue.append(idx)
            for k in queue:
                find_l(k)
                del rate(n)

def find_l(last_):
    for k,idx in enumerate(rate[last_]):
        if k == max(rate[last_]):
            return name[idx]
        
def dict_reverse(dict_l):
    sorted_values= sorted(dict_l.values())
    sorted_dict = {}
    for i in sorted_values:
        for k in dict_l.keys():
            if dict_1[k] == i:
                sorted_dict[k] = dict_1[k]
                break
    
n = 3
name = ["John Doe","Jane Smiths","Jane Austen"]
rating = [[1,2,3],[2,1,3],[2,3,1],[1,2,3],[3,1,2]]
print(solution(n,name,rating))
