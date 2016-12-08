def even_odd(n):
    if n % 2 == 0:
        print n, "is even."
    else:
        print n, "is odd."
        even_odd(n-1)

def countdown(n):
    if n == 0:
        print "Blast off!"
    else:
        print n
        countdown(n-1)

# even_odd(5)
# countdown(3)

def check_test():
    prompt = "How are you feeling?\n"
    answer = input(prompt)

# check_test()

def greater_less(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

print greater_less(-2)
print greater_less(0)

