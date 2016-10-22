with open('input.txt') as f:
    data = f.readlines()
total = 0
x = '0'
for line in data:
	total += int(x)
	x = '0'
	for char in line:
		if char.isnumeric():
			x += str(char)
		elif char == "-":
			x = '-'
		else:
			total += int(x)
			x = '0'

print(total)