def symmetric(myList):
    # Your code here
    length = len(myList) #gets length of the list, aka the column
    len2 = len(myList[0]) #gets length of list's first list - the row
    if(len2==length): #if column length != row length, return false
	    x = 0 #x = row value
	    while x<length: #because row's range is 0:2, and length is 3
	        if myList[x][0]!=myList[0][x]:
	    		return False
	    	x+=1
	    return True
	    		
	# return False



    
            

print symmetric([[1, 2, 3],
               [1, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
               ["dog", "dog", "fish"],
               ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])