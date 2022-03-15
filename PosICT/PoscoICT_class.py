class Candidate:
    cnt = 0
    def __init__(self, name):
        self.name = name
        Candidate.cnt += 1
        self.number = Candidate.cnt
        self.score = 0

    def __lt__(self, other):
        return self.score < other.score

#input data for each variable
data = '3\nJohn Doe\nJane Smith\nJane Austen\n1 2 3\n2 1 3\n2 3 1\n1 2 3\n3 1 2'
data = data.split('\n')
N = int(data[0])
cands = {Candidate(name) for name in data[1:N+1]}
votes = [[int(y) for y in x.split()] for x in data[N+1:]]

#logic
while len(cands) > 1:    
    for c in cands:  # 집계
        c.score = [v[0] for v in votes].count(c.number)
        if c.score >= 50 + (N is 2): 
            print(c.name); exit()  # 당선
    print(min(cands).name)
    minvotes, maxvotes = min(cands).score, max(cands).score
    if minvotes == maxvotes: break  # 전부 동률    
    loosers = {c for c in cands if c.score == minvotes}  # 탈락자
    cands = cands - loosers    
    #let's see confusing
    votes = [v if v[0] not in [c.number for c in loosers] else v[1:] for v in votes] # 다음 순위 득표
    print(votes,[c.number for c in loosers])
print([c.name for c in cands])
