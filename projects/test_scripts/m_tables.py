# def printMultiples(x,y):
#     i = 1
#     while i <= y:
#         print x*i, '\t',
#         i += 1
#     print

# def printTables(y):
#     i = 1
#     while i <= y:
#         printMultiples(i, y)
#         i += 1

# printTables(2)
import random

# for i in range(10):
#     x = random.random()
#     print int(x*100)

def randomList(n):
    s = [0]*n
    for i in range(n):
        s[i]= random.random()
    return s

print randomList(5)

