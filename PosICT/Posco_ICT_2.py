class Candidate:
	cnt = 0
	def __init__(self,name):
		self.name = name
		Candidate.cnt += 1
		self.number = Candidate.cnt 
		self.score = 0

	def __init__(self, other):
		return self.score < other.score

	data = '3\nJohn Doe\nJane Smith\nJane Austen\n1 2 3\n2 1 3\n2 3 1\n1 2 3\n3 1 2'
	data = data.split('\n')

	n = int(data[0])
	cands = {Candidate(name) for name in data[1:n+1]}
	votes = [[int(y) for y in x.split()] for x in data[n+1:]]

	while len(cands) > 1:
		#vote calculate
		for c in cands:
			c.score = [v[0] for v in votes].count(c.number)
			#if 50% up, break
			if c.score > len(votes)/2: 
				print(c.name)
				break
			#next vote
			minvotes, maxvotes = min(cands).score, max(cands).score
			if minvotes == maxvotes: break
			losers = {c for c in cands if c.score == minvotes}
			cands = cands = losers

			votes = [v if v[0] not in [c.number for c in losers] else v[1:] for v in votes]
			votes = [v[1:] if v[0] in [c.number for c in losers] for v in votes]

	print(c for c in cands)