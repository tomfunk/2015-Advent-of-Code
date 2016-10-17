from string import ascii_lowercase
alpha = []#list of all letters
inc = []#list of increasing straights
bawal = ['i','o','l']#list of forbidden characters
pairs = []#list of pairs
password = 'hepxxzaa'#password to be tested

for letter in ascii_lowercase:
	alpha.append(letter)

for a in range(24):
	inc.append(alpha[a]+alpha[a+1]+alpha[a+2])
	
for a in alpha:
	pairs.append(a+a)

def iterate(input):
	beg = input
	output = ''
	roll = True
	while len(beg) > 0:
		beg, end = beg[:-1], beg[-1]
		if roll:
			if end == 'z':
				roll = True
				output = 'a' + output
			else:
				roll = False
				output = alpha[alpha.index(end)+1] + output
		else:
			output = end + output
	return output	
	
def check(input):
	score = 1
	for a in pairs:
		if a in input:
			score += .5
	for a in inc:
		if a in input:
			score += 1
			break
	for a in bawal:
		if a in input:
			score -= 5
	return score

#recursion depth exceeded
'''
def runner(password):
	print(password, check(password))
	if check(password) >= 3:
		print(password)
	else:
		runner(iterate(password))
runner(password)
'''
while True:
	if check(password) >= 3:
		print(password,check(password))
		break
	else:
		password = iterate(password)
		#print(password,check(password))

