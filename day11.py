def checkio(data):
	ans = ''
	x = 0
	Nums = [['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
	while x < 11:
		if data - Nums[x][1] >= 0:
			data -= Nums[x][1]
			ans += Nums[x][0]
		else:
			x += 1
	return(ans)
	
checkio(1300)