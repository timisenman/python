### Stacks ###

#Client: A program (or the person who wrote it) that uses an ADT.

#Provider: The code (or the person who wrote it) that uses an ADT. 

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return (self.items == [])

# one = Stack()
# one.push(1)
# one.push(2)
# one.push(5)
# one.push(3)
# one.push(4)

# print one.items

# while not one.isEmpty():
#     print one.pop(),

def evalPostfix(expr):
    import re
    tokenList = re.split("([^0-9])", expr)
    stack = Stack()
    for token in tokenList:
        if token == '' or token == ' ':
            continue
        if token == '+':
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
        return stack.pop()

print evalPostfix ("56 47 2 *")
#doesn't actually print the result, which should be 206
