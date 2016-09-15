# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
    #the function will work like this, for fibonacci(10):
    # fibonacci(10-1) + fibonacci(10-2) = 9 + 8
    # fibonacci(9-1) + fibonacci(9-2) = 8 + 7
    # fibonacci(8-1) + fibonacci(8-2) = 7 + 6
    # fibonacci(7-1) + fibonacci(7-2) = 6 + 5
    # fibonacci(6-1) + fibonacci(6-2) = 5 + 4
    # fibonacci(5-1) + fibonacci(5-2) = 4 + 3
    # fibonacci(4-1) + fibonacci(4-2) = 3 + 2
    # fibonacci(3-1) + fibonacci(3-2) = 2 + 1
    # fibonacci(2-1) + fibonacci(2-2) = 1 + 0
    # and once n==1, will just add 1, and when 0, add 0.


def fibonacci(n):
	current = 0
	after = 1
	for i in range(0, n):
		current, after = current, current + after
	return current



print fibonacci(0)
#>>> 0
print fibonacci(1)
#>>> 1
print fibonacci(15)
#>>> 610