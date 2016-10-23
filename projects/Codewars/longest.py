letters = "abcdefghijklmnopqrstuvwxyz"
def longest(a,b):
    lis = []
    for i in a and b:
    	print i
        lis.append(i)
        #still must solve for duplicates!
    lis.sort()
    lis = ''.join(set(lis))
    return lis

print longest("aretheyhere", "yestheyarehere")

print "Should be: aehrsty"