### Trees ###
class Tree:
    def __init__(self, cargo=None, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


    def total(tree):
        if tree == None: return 0
        return total(tree.left) + total(tree.right) + tree.cargo

left = Tree(2)
right = Tree(3)
tree = Tree(1,left, right)
#OR
tree = Tree(1, Tree(2), Tree(3))
#print tree.left.left, "none"

#print total(tree), "6"

### Expression Trees ###
#Use them to evaluate expressions

#1 + 2 * 3
exTree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))

def printTreeInOrder(tree):
    if tree == None: return
    #infix
    printTreeInOrder(tree.left)
    print tree.cargo,
    printTreeInOrder(tree.right)

def printTreePreOrder(tree):
    if tree == None: return
    print tree.cargo,
    printTreePreOrder(tree.left)
    printTreePreOrder(tree.right)

    #postfix
def printTreePostOrder(tree):
    if tree == None: return
    printTreePostOrder(tree.left)
    printTreePostOrder(tree.right)
    print tree.cargo,

#printTree(exTree)

### Graphical Representation of the Tree ###

def printTreeIndented(tree, level=0):
    if tree == None: return
    printTreeIndented(tree.right, level+1)
    print ' '*level + str(tree.cargo)
    printTreeIndented(tree.left, level+1)

#printTreeIndented(exTree)

### Building an expression tree ###

def getToken(tokenList,expected):
    if tokenList[0] == expected:
        del tokenList[0]
        return True
    else:
        return False

def getNumber(tokenList):
    x = tokenList[0]
    if not isinstance(x,int): return None
    del tokenList[0]
    return Tree(x, None, None)

# def getProduct(tokenList):
    a = getNumber(tokenList)
    if getToken(tokenList, '*'):
        b = getNumber(tokenList)
        return Tree('*', a, b)
    else:
        return a


#for longer lists, change to:
def getProduct(tokenList):
    a = getNumber(tokenList)
    if getToken(tokenList, '*'):
        b = getProduct(tokenList) #change to getProduct
        return Tree('*', a, b)
    else:
        return a

def getSum(tokenList):
    a = getProduct(tokenList)
    if getToken(tokenList, '+'):
        b = getProduct(tokenList)
        return Tree('+', a, b)
    else:
        return a

def getNumber(tokenList):
    if getToken(tokenList, '('):
        x = getSum(tokenList)
        getToken(tokenList, ')')
        return x
    else:
        x = tokenList[0]
        if not isinstance(x, int): return None
        tokenList[0:1] = []
        return Tree(x, None, None)



tokenList = [9, '*', 11, 'end']
x = getProduct(tokenList)
printTreePostOrder(x)

print

tokenList = [9, '+', 11, 'end']
x = getProduct(tokenList)
printTreePostOrder(x)

print

tokenList = [3, '*', 5, '*', 13, 'end']
x = getProduct(tokenList)
printTreeInOrder(x)
print
printTreePostOrder(x)

print
tokenList = [9, '*', 11, '+', 5, '*', 7, 'end']
tree = getSum(tokenList)
printTreePostOrder(tree)

print
tokenList = [9, '*', '(', 11, '+', 5, ')', '*', 7, 'end']
tree = getSum(tokenList)
printTreePostOrder(tree)

