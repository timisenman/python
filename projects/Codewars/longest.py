def longest(a,b):
    lis = []
    for i in a and b:
        lis.append(i)
        #still must solve for duplicates!
    lis.sort()
    lis = ''.join(lis)
    return lis


print testing("aretheyhere", "yestheyarehere")
print "Should be: aehrsty"