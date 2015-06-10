import math

# Find longest side of
# right-angled triangle

def square(x):
	return x * x

def sqrt(x, guess):
	def closeEnough(x, guess):
		if math.fabs(square(guess) - x) > 0.01:
			return True
		else:
			return False

	def improveGuess(x, guess):
		return (((x / guess) + guess) / 2)

	while closeEnough(x, guess):
		guess = improveGuess(x, guess)
	return guess

def pythag(a, b):
	a2b2 = square(a) + square(b)
	return sqrt(a2b2, 1.0)

print pythag(2, 3)