class Item(object):
	def __init__(self, n, v, w):
		self.name = n
		self.value = v
		self.weight = w
	def get_name(self):
		return self.name
	def get_value(self):
		return self.value
	def get_weight(self):
		return self.weight
	def __str__(self):
		result = '<' + self.name + ', ' + str(self.value) +', '\
				+ str(self.weight) + '>'
		return result

def build_items():
	names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
	values = [175, 90, 20, 50, 10, 200]
	weights = [10, 9, 4, 2, 1, 20]
	items = []
	for i in range(len(values)):
		items.append(Item(names[i], values[i], weights[i]))
	return items

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
	
def choose_best(p_set, max_weight, get_val, get_weight):
	best_val = 0.0
	best_set = None
	for items in p_set:
		items_val = 0.0
		items_weight = 0.0
		for item in items:
			items_val += get_val(item)
			items_weight += get_weight(item)
		if items_weight <= max_weight and items_val > best_val:
			best_val = items_val
			best_set = items
	return (best_set, best_val) 

def test_best(max_weight = 20):
	items = build_items()
	p_set = genPowerSet(items)
	taken, val = choose_best(p_set, max_weight, Item.get_value, Item.get_weight)
	print('Total value of item taken is ', val)
	for item in taken:
		print(item)

test_best()
