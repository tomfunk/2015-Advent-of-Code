import itertools

with open('input.txt') as f:
    content = f.readlines()

dest = []
dists = []
mindist = 0
for x in content:
	x = x.strip('\n')
	x = x.strip('to')
	x = x.strip('=')
	x = x.split(' ')
	dists.append(x)
	if not x[0] in dest:
		dest.append(x[0])
	if not x[2] in dest:
		dest.append(x[2])
ln = len(dest)
combo = list(itertools.permutations(dest, ln))

def finddist(route):
	ans = 0
	for x in range(len(route)-1):
		for y in dists:
			if y[0] == route[x] and y[2] == route[x+1]:
				ans += int(y[4])
			elif y[2] == route[x] and y[0] == route[x+1]:
				ans += int(y[4])
	return ans
			
#print(finddist(combo[0]))

for route in combo:
	dist = finddist(route)
	if dist > mindist:
		mindist = dist
		print(mindist,route)