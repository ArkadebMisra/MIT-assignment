#newton-raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 25
guess = k/2.0
numguess = 0
while abs(guess*guess - k)>= epsilon:
	print(guess)
	numguess += 1
	guess = guess - (((guess**2) - k)/(2*guess))
print("Square root of ",k ,"is about ",guess)
print("numguess=",numguess)
