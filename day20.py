houses = 100000
max = 34000000
gifts = 0
'''
while gifts < max:
	houses += 1
	#for house in range(1,houses):
	gifts = 0
	for elf in range(1,houses):	
		if houses % elf == 0:
			gifts += elf*10
'''
from math import sqrt
def factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result
	
while gifts < max:
	houses += 1
	gifts = 0
	for factor in factors(houses):
		if factor * 50 >= houses:
			gifts += factor * 11

print('House # %d gets %d gifts' % (houses, gifts))