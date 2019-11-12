#SEARCH ALGORITHMS.............................................................

#SIMPLE SEARCH..................................

# ~ def search(L, e):
	# ~ """Assumes L is a list, the elements in the list
	# ~ are in assending order
	# ~ Retirn True if e in L , False otherwise"""
	# ~ for i in range(len(L)):
		# ~ if L[i] == e:
			# ~ return True
		# ~ if L[i] > e:
			# ~ return False
	# ~ return False
	
# ~ L = [1, 2, 3, 4, 5, 6,]
# ~ print(search(L, 7))


#BINARY SEARCH.....................................

def search(L,e):
	"""Assumes L is a list , the elements of which 
	are in assending order
	Returns True if e is in L , False otherwise"""
	
	def binSearch(L, e, low, high):
		#Dicrements high - low
		
		if high == low:
			return L[low] == e
		mid = (low + high)//2
		if L[mid] == e:
			return True
		elif L[mid] > e:
			if low == high:
				return False
			else:
				return binSearch(L, e, low, mid-1)
		else:
			return binSearch(L, e, mid+1, high)
			
	if len(L) == 0:
		return False
	else:
		return binSearch(L, e, 0, len(L)-1)


# ~ L = 'abcdefghijklmnopqrstuvwxy'
# ~ print(search(L, 'z'))


#SORT ALGORITHMS..................................................................
#SELECTION SORT..........................................

# ~ def selSort(L):
	# ~ """Assumes L is a list of elements that can be  compared using >/<.
	# ~ sort L in assnding order"""
	# ~ suffixStart = 0
	# ~ while suffixStart != len(L):
		# ~ #look at the elelments at the  suffix
		# ~ for i in range(suffixStart, len(L)):
			# ~ if L[i] < L[suffixStart]:
				# ~ #Swap the position of the elements
				# ~ L[suffixStart], L[i] = L[i] , L[suffixStart]
		# ~ suffixStart += 1
	# ~ return L
		
# ~ L = [1, 5, 3, 4, 2, 0, 10]

# ~ array = selSort(L)
# ~ print(array)	


#MERGE SORT...............................................


def merge(left, right, compare):
	"""Assumes left and right are sorted list and
		compare defines an ordering of the elements
	Returns a new sorted(by compare) list containing
		the same elements as (left + right) would contain""" 
		
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if compare(left[i], right[j]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
		
	while (i < len(left)):
		result.append(left[i])
		i += 1
	while(j < len(right)):
		result.append(right[j])
		j += 1
	return result
	
def mergeSort(L, compare = lambda x,y : x < y):
	"""Assumes L is a list, compare defines an ordering on elements of L
		return a new sorted list with the same elements of L"""
	
	if len(L) < 2:
		return L[:]
	else:
		middle = len(L)//2
		#print('partition Left ',L[:middle])
		#print('partition Right ',L[middle:])
		left = mergeSort(L[:middle], compare)
		right = mergeSort(L[middle:], compare)
		#print('left ', left)
		#print('right ', right)
		#print('merged ',merge(left, right, compare))
		return merge(left, right, compare)
		
# ~ L = [2, 1, 5, 4,3]
# ~ print(mergeSort(L))




int_list = [2,1,5,4,3,6,8,7,9,10,15,26,18,56,60,42,56,64]

print(search(mergeSort(int_list),15))
