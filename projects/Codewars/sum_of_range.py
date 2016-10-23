#sum of 1 through a number n

def f(n):
	if n < 0 or n % 1 != 0:
		return None
	return sum([i for i in range(1,n+1)])

print f(100)
print f(-1)
print f(2.5)
print f(10)