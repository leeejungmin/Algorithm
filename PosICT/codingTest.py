def solution(n,name,rating):
    cnt=0
    name_n=dict()
    rate = [0 for _ in range(n+1)]
    live_m = [1 for _ in range(n+1) ]
    rate_d = dict()
    dead = []
    #make list memeber of dictionary
    for n,idx in enumerate(name):
        name_n[n] = idx
    
    #compare the most rate
    for i in rating:
        a = rate[i[0]]
        rate[i[0]] = a + 1
    for idx,r in enumerate(rate):
        if idx == 0:
            continue
        rate_d[name[idx-1]] = r
        
    sorted_rate = sorted(rate_d.items(), key = lambda x: x[1],reverse=True)
    print(next(iter(sorted_rate))[0])

    #if more than half
    if max(rate) > (len(rating)/2):
        return next(iter(sorted_rate))[0]
    else:
        for key,value in rate_d.items():
            print(key,value,rate.sort(reverse=True))
            if value == rate.sort()[1]:
                dead.append(key)
                live_m[name_n[key]] = False
        for k in dead:
            print(name_n(k))
            #check max in list
            
            for idx,j in enumerate(rate[k]):
                if j == max(rate[k]):
                    return name[idx]
##            del rate(n)

def find_l(last_):
    for k,idx in enumerate(rate[last_]):
        if k == max(rate[last_]):
            return name[idx]
        
def dict_reverse(dict_l):
    sorted_values= sort(dict_l.values())
    sorted_dict = {}
    for i in sorted_values:
        for k in dict_l.keys():
            if dict_1[k] == i:
                sorted_dict[k] = dict_1[k]
                break
q = [1,5,3,2]
print(sorted(q,reverse=True))

n = 3
name = ["John Doe","Jane Smiths","Jane Austen"]
rating = [[1,2,3],[2,1,3],[2,3,1],[1,2,3],[3,1,2]]
print(solution(n,name,rating))

#make dictionary list
#compare most > least
#at least , least member-> false > check true> compare most

