#Classes
class Point:
    pass

#To create a new instance of Point, call it by a function:
new = Point()

#Add new data to an instance (called Attributes):
new.x = 5
new.y = 10
x = new.x

print new.x
print new.y
print x

print '(' + str(new.x) + ',' + str(new.y) + ')'
print new

def printPoint(p):
    print '(' + str(p.x) + ',' + str(p.y) + ')'

printPoint(new) 

#reference
p1 = Point()
p1.x = 3
p1.y = 4
p2 = Point()
p2.x = 3
p2.y = 4
print p1 is p2

#assignment creates aliases of the same object 
p2 = p1
print p1 is p2

def samePoint(p1,p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

print samePoint(p1,p2)

print "--------"

class Rectangle():
    pass

box = Rectangle()
box.width = 100.0
box.height = 200.0

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

print box
print box.corner

def findCenter(box):
    p = Point()
    p.x = box.corner.x + box.width/2.0
    p.y = box.corner.y - box.height/2.0
    return p

center = findCenter(box)
printPoint(center)


def growRect(box, dwidth, dheight):
    box.width = box.width + dwidth
    box.height = box.height + dheight

bob = Rectangle()
bob.width = 100.0
bob.height = 200.0
bob.corner = Point()
bob.corner.x = 0.0
bob.corner.y = 0.0
growRect(bob, 50, 100)

growRect(bob, 50, 100)
printPoint(center)