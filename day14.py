class reindeer(object):
	def __init__(self, speed, burst, rest, dist = 0.0, score = 0.0):
		self.speed = speed
		self.burst = burst
		self.rest = rest
		self.dist = dist
		self.score = score
		
	def race(self, time):
		rem = time%(self.burst + self.rest)
		full = time - rem
		self.dist = self.speed*self.burst*full/(self.burst+self.rest)+min(rem,self.burst)*self.speed
	
Vixen = reindeer(19, 7, 124)
Rudolph = reindeer(3, 15, 28)
Donner = reindeer(19, 9, 164)
Blitzen = reindeer(19, 9, 158)
Comet = reindeer(13, 7, 82)
Cupid = reindeer(25, 6 , 145)
Dasher = reindeer(14, 3, 38)
Dancer = reindeer(3, 16, 37)
Prancer = reindeer(25, 6, 143)

lead = [Vixen, Rudolph, Donner, Blitzen, Comet, Cupid, Dasher, Dancer, Prancer]

for y in range(1,2504):
	max = 0
	for x in lead:
		x.race(y)
		if x.dist > max:
			max = x.dist
	for x in lead:
		if x.dist == max:
			x.score += 1
			
for x in lead:
	print(x.score)
