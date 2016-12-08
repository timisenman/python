### The Animal Tree ###
class Tree:
    def __init__(self, cargo=None, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def animal():
    #singleton
    root = Tree('bird')

    while 