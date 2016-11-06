class ingredient(object):
	def __init__(self, capacity, durability, flavor, texture, calories):
		self.capacity = capacity
		self.durability = durability
		self.flavor = flavor
		self.texture = texture
		self.calories = calories
			
Frosting = ingredient(4, -2, 0, 0, 5)
Candy = ingredient(0, 5, -1, 0, 8)
Butterscotch = ingredient(-1, 0, 5, 0, 6)
Sugar = ingredient(0, 0, -2, 2, 1)

Igs = [Frosting, Candy, Butterscotch, Sugar]

max = 0

for F in range(101):
	for C in range(101-F):
		for B in range(101-F-C):
			for S in range(101-F-C-B):
				cap = F * Frosting.capacity + C * Candy.capacity + B * Butterscotch.capacity + S * Sugar.capacity
				dur = F * Frosting.durability + C * Candy.durability + B * Butterscotch.durability + S * Sugar.durability
				fla = F * Frosting.flavor + C * Candy.flavor + B * Butterscotch.flavor + S * Sugar.flavor
				tex = F * Frosting.texture + C * Candy.texture + B * Butterscotch.texture + S * Sugar.texture
				
				if cap < 0:
					cap = 0
				if dur < 0:
					dur = 0
				if fla < 0:
					fla = 0
				if tex < 0:
					tex = 0
				
				score = cap * dur * fla * tex
				
				if score > max and (F+C+B+S) == 100:
					max = score
					print(F,C,B,S)
					print(score)
