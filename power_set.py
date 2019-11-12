def getBinaryRep(n, numDigits):
	"""Assumes n and numDigits are non negetive int
	return a str of length numdigits that is a 
	binary representation of n"""
	result = ''
	while n > 0:
		result = str(n%2) + result
		n=n//2
	if len(result) > numDigits:
		raise ValueError("not enough digits""")
	for i in range(numDigits - len(result)):
		result = '0' + result
	return result
	
def genPowerSet(L):
	"""Assumes L is a list
	Returns a list of list that contains all
	possible combination of  the elments"""
	
	powerset = []
	for i in range(0, 2**len(L)):
		binStr = getBinaryRep(i,len(L))
		subset = []
		for j in range(len(L)):
			if binStr[j] == '1':
				subset.append(L[j])
		powerset.append(subset)
		
	return powerset
	
list = 'abcdefghij'

print(genPowerSet(list)) 
