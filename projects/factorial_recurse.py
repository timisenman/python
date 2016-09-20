#Recursion

factorial(0) = 1
factorial(n) = n * factorial(n-1) #where any integer is greater than 0

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

#here is the process beneath the code

#factorial(3)
	#if 3 == 0:
		#return 1
	#else:
		#return 3 * factorial(3-1) = 6
		#...
		#return 2 * factorial(2-1) = 2
		#return 1 * factorial(1-1) = 1
		#return 0 * factorial(0)   = 
			#makes the if statement True
			#returns 1