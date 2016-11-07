from itertools import combinations

conts = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
total = 0
for y in range(len(conts)):
	for x in combinations(conts,y+1):
		if sum(x) == 150:
			total += 1

print(total)