import math, sys

def sqrt(number, accuracy=5):
	"""
	implemented sqrt using newton's method
	Let's say we want to find square-root of n
	So x^2 = n, hence we find roots of that using newton's method
	We have:
	f(x) = x^2 - n 
	f'(x) = 2x
 	x1 = x0 - f(x0)/f'(x0)
 	x2 = x1 - f(x1)/f'(x1)
 	.
 	.
 	we stop after reaching the desired tolerance.
 	The default tolerance is 10^(-5) digits
	"""

	try:
		number = float(number)
	except ValueError:
		print "Input is not a number"
		sys.exit(1)

	# I can raise a value error here,
	# but the convention seems to be to return NaN (not a number)
	# NaN's are part of IEEE 754 floating point standard
	# and are standard as of python 2.6
	if number < 0:
		return float('nan')
	
	# tolerance : 10 ^ (-accuracy)
	tol = 10 ** (-1 * accuracy) 

	# x0: initial guess, average
	x0 = (number + 1)/2.0 
	result = x0

	while math.fabs((result ** 2) - number) >= tol:
		result = result - ((result ** 2 - number) / (2 * result))

	return result

if __name__ == '__main__':
	if len(sys.argv) < 2:
		sys.exit('Usage: %s <number>' % sys.argv[0])
	print sqrt(sys.argv[1])