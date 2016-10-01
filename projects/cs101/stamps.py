# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

#positive integer
#return pence: 5p, 2p, 1p
#retun list in a {tuple} of {1, 2, 3} numbers {#5p, #2p, #1p}
#use mostly 5p, then 2p, then 1p - find numbers divisible by each


def stamps(n):
    #ask for number. is >= 5? 
    count_5 = 0
    count_2 = 0
    count_1 = 0
    while n >= 5:
    	#subtract 5.
    	n = n - 5
    	#record # of subtractions - count_5
    	count_5 = count_5 + 1
    #ask for number. is >= 2?
    while n >= 2:
    	#subtract 2 - count_2
    	n = n - 2
    	#record # of subtractions
    	count_2 = count_2 + 1
    #ask for number. is >= 1?
    while n == 1:
    	#subtract 1 - count_1
    	n = n - 1
    	#record # of subtractions
    	count_1 = count_1 + 1
    #if 0, print totals in tuple
    if n == 0:
    	#print (count_5, count_2, count_1)
    	return count_5, count_2, count_1
    	


print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps