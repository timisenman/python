class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next
    
    def __str__(self):
        return str(self.cargo)

    def printBackward(list):
        if list == None: return
        tail = self.next
        tail.printBackward()
        print self.cargo,

    
    
node = Node("test")
print node

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

print node1, node2, node3

node1.next = node2
node2.next = node3
node3.next = node3



def printList(node):
        lis = []
        while node:
            lis.append(node.cargo)
            node, 
            node = node.next
        print lis


printList(node3)

class LinkedLists:
    def __init__(self):
        self.length = 0
        self.head = None

    # def printBackward(self):
    #     print "[",
    #     if self.head != None:
    #         self.head.printBackward()
    #     print "]",

    def addFirst(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length + 1
    
    
# link = LinkedLists()



# # printList(node1)
# # printBackward(node1)

# #Infinite loop
# #printList(node3)
# link.addFirst(1)
# link.printBackward()