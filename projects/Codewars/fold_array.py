def fold_array(a, f):
    folds = f
    new = a

#     if len(new) == 1:
#         return [new[0]]
#     if len(new) == 0:
#         return []

    for l in range(folds):
        temp = []
        for i in range(0, int(len(new)/2)):
            temp.append(new[i]+new[-i-1])
        if len(new) % 2 != 0:
            temp.append(new[int(len(new)/2)])
        new = temp
    return new

print fold_array([2,2,2,2,2], 4)