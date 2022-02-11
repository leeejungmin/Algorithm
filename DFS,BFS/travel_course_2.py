def solution(tickets):
    global ans
    ans=[]
    
    dic_=dict(tickets)
    dfs(dic_)
    return ans

def dfs(dic_):
    stack=["ICN"]
    ans=["ICN"]
    while stack!=None:
        cur_=stack.pop()
        next_=dic_.get(cur_)
        #anaylize from result
        if next_ == None:
            continue
        stack.append(next_)
        ans.append(next_)
        cur=0
        next_=0
        print(ans,stack)
        
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
#tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
#print(dict(tickets))

#for i in dict(tickets).keys():
#   dict(tickets)[i].sort(reverse=True)
#for i in dict(tickets).values():
#    print(i)
print(solution(tickets))
