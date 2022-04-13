def fact(n):
	a = 1
	for i in range(1,n+1):
		a = a * i 
		if i == n :
			return a

def roots(a, b, c):
	from cmath import sqrt 
	delta = (b**2 - (4*a*c))
	racine = sqrt(delta)
	x1 = (-b + racine)/2*a
	x2 = (-b - racine)/2*a
	res = (x1,x2)
	return res 

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
