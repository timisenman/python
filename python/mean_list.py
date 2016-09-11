def mean(lis):
	total = 0
	length = len(lis)
	for i in lis:
		total = total+i
	return total/length

print mean([1,2,3,4,5])
#>>>2.5

#get total number of list numbers
#get all numbers in the list
#add each number together to create a sum
#divide list_sum by length