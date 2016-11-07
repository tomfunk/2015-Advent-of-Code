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
	#print(sue[1], sue[2], getattr(SuePrime, sue[1]))
	if getattr(SuePrime, sue[1]) == int(sue[2]) and getattr(SuePrime, sue[3]) == int(sue[4]) and getattr(SuePrime, sue[5]) == int(sue[6]):
		print(sue[0])

