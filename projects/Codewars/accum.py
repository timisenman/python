def accum(a):
    
    new = list(enumerate(a))
    final = []

    for i in new:
        temp = int(i[0]+1) * i[1]
        final.append(temp[0].capitalize() + temp[1:].lower())
    
    return '-'.join(final)


print accum('abc')
print "-------"
print accum("pglnRxqenU")