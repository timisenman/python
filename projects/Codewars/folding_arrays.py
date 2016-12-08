# take an array
# find the center
# remove the center
# create two lists
# reverse the second list 
# add the two together
# return folded

# or

# initialize a countdown for folds
# take an array
# if the index.array is > 1
# 	add first item to last in new array
# if index.array == 1
# 	return new array

def fold(a,f):
	folds = f
	new = []
	# print ("initialize")
	if len(a) == 1:
		return new
	while folds > 0:
		while len(a) > 1:
		#add first item to last in new array
			new.append([a[0]+a[-1]])
			folds -= 1
			# print ("new " + new)
	return new
	

	
a = [1,2,3] 
print fold(a,1)
# def fold(array):
# 	length = index.array
# 	middle = length / 2
# 	arr = array.split()
# 	front = [:middle]
# 	back = [middle:]
