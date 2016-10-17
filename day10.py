start = 3113322113
numlist = [str(start)]
def mixer(start):
	ans = ""
	x = 1
	for y in range(len(start)):
		#print(str(start)[y])
		if y == len(start)-1:
			ans += str(x) + str(start)[y]
		elif str(start)[y] == str(start)[y+1]:
			x +=1
		else:
			ans += str(x) + str(start)[y]
			x=1
	numlist.append(ans)	

for x in range(50):
	mixer(numlist[-1])
	
print(len(numlist[-1]))