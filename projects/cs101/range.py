# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

#range is the difference between the highest value and lowest value in a set of 
#numbers. i.e.: (1, 3, 10) range = 9, 10-1

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def smaller(a,b):
    if a > b:
        return b
    else:
        return a

def smallest(a,b,c):
    return smaller(a, smaller(b,c))

def set_range(a,b,c):
    #find biggest value in the set
    return biggest(a,b,c) - smallest(a,b,c)
    #find the smallest value in the set

    #subtract the biggest from the smallest


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6