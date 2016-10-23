# In this little assignment you are given a string of space 
# separated numbers, and have to return the highest and lowest number.

#high_and_low("1 2 3 4 5")  # return "5 1"

# def high_and_low(numbers):
# 	high = max(numbers.split())
# 	low = min(numbers.split())
# 	return str(high) + " " + str(low)

# print high_and_low("1, 2, 3, 4, 5")

# def high_and_low(numbers):
# 	res = numbers.split()
#     high = max(int(res))
#     low = min(int(res))
#     return str(high) + " " + str(low)

def high_and_low(numbers):
	res = numbers.split()
	res = [int(s) for s in numbers.split()]
	high, low = max(res), min(res)
	return str(high) + " " + str(low)


#num = ['4', '5', '29', '54', '4', '0', '-214', '542', '-64', '1', '-3', '6', '-6']
num = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"

print high_and_low(num)

