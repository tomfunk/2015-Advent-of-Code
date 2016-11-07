with open('input.txt') as f:
    content = f.readlines()

hoa = []

for x in content:
	x = x.strip('\n')
	x = x.replace(' ','')
	x = x.replace(':',',')
	x = x.split(',')
	hoa.append(x)
	
class aunt(object):
	def __init__(self, children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes):
		self.children = children
		self.cats = cats
		self.samoyeds = samoyeds
		self.pomeranians = pomeranians
		self.akitas = akitas
		self.vizslas = vizslas
		self.goldfish = goldfish
		self.trees = trees
		self.cars= cars
		self.perfumes = perfumes

SuePrime = aunt(3,7,2,3,0,0,5,3,2,1)

for sue in hoa:
	score = 0
	for x in range(1,4):
		y = x*2
		if sue[y-1] == 'cats' or sue[y-1] == 'trees':
			if getattr(SuePrime, sue[y-1]) < int(sue[y]):
				score += 1
		elif sue[y-1] == 'pomeranians' or sue[y-1] == 'goldfish':
			if getattr(SuePrime, sue[y-1]) > int(sue[y]):
				score += 1
		else:
			if getattr(SuePrime, sue[y-1]) == int(sue[y]):
				score += 1
		
	if score == 3:
		print(sue[0])

