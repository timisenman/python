def reverse(s):
    new = list(s)
    
    import time
    # start = time.time()
    # rev = []
    # for i in range(len(new)):
    #     rev.append(new.pop())
    # print ''.join(rev)
    # end = time.time()
    # print "Tim's code:", (end-start)

    jstart = time.time()
    left = 0
    right = len(new)-1
    while left < right:
        new[left], new[right] = new[right], new[left]
        left, right = left + 1, right - 1
    print ''.join(new)
    jend = time.time()
    print "Jack's code:", (jend-jstart)
        
    

reverse("hello")
# print reverse('reverse')