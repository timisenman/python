# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

def union(a,b):
	#e assumes all values in 'a'
	for e in a:
		#check is all values of e are in 'b'
		if e not in b:
			#if e is not in b, add b.
			#here, you are only adding the missing values
			#of a to b, 
			b.append(e)


# To test, uncomment all lines 
# below except those beginning with >>>.

a = [1,2,3]
b = [2,4,6]
print union(a,b)
print a 
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]
