def longest(a,b):
	letters = "abcdefghijklmnopqrstuvwxyz"
	result = ""
    for c in letter:
    	if c in a and in b:
    		result += c
    return result

print longest("aretheyhere", "yestheyarehere")

print "Should be: aehrsty"