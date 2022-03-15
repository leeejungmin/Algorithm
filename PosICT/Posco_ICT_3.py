class Candidate:
	def __init__(self):
		self.name = name
		self.score = score
		self.number = number

	def __lt__(self, other):
		return self.score > other.score

	data = '3\nJohn Doe\nJane Smith\nJane Austen\n1 2 3\n2 1 3\n2 3 1\n1 2 3\n3 1 2'
	data = data.split('\n')

	n = data[0]
	#check
	candidate = Candidate() 
	cands = [candidate.number,candidate.name for idx, name in enumerate(data[1:n+1])]
	votes = [int(y) for y in x.split("")] for x in data[n+1:]

	while len(cands) > 1:
		#how many votes for each cand
		for c in cands:
			c.score = [v[0] for v in votes].count(c.number)

		if c.score > len(votes): return c.name  

		#find min
		minvotes = min(cands).score
		maxvotes = max(cands).score
		
		loser = [c for c in cands if c.score == minvotes]
		cands = cands = loser

		#now just think hierachical
		#votes = [v[1:] for v in votes if votes[0] == loser.number]
		votes = [v[1:] if votes[0] in [c.number for c in loser] for v in votes

		for v in votes:
			if v[0] in [c.number for c in loser]:
				votes = v[1:]

	print(c.name for c in cands)