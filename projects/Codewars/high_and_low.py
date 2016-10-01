# In this little assignment you are given a string of space 
# separated numbers, and have to return the highest and lowest number.

#high_and_low("1 2 3 4 5")  # return "5 1"

def high_and_low(numbers):
	return str(max(numbers.split()))+" "+str(min(numbers.split()))

print high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")

str(max("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6".split()))

"4 5 29 54 4 0 -214 542 -213 -64 1 -3 6 -6".split()