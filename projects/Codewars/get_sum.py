# # Given two integers, which can be positive and negative, find the sum of all the numbers between including them too and return it. If both numbers are equal return a or b.

# # Note! a and b are not ordered!

# def get_sum(a,b):
# 	if a == b:
# 		return b
# 	lis = range(a,b)
# 	print lis
# 	return sum(lis)+b 

# print get_sum(-2,4)
# #-2,-1,0,1,2,3,4

# #print get_sum(0,-1)

# print get_sum(-2,2)

def get_sum(a,b):
	if a == b:
		return b
	if a > b:
		return sum(range(b,a),a)
	return sum(range(a,b),b)

print get_sum(1,3)
print ">>>6"
print get_sum(5,-2)
print ">>>12"
