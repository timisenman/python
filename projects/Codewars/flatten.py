def flatten(lis):
    new = []
    for i in lis:
        if isinstance(i, list):
           for j in i:
               new.append(j)
        else:
            new.append(i)
    return new



print flatten([1,2])
print flatten([[1,2], 3])

### Success! ###