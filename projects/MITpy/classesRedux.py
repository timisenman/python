class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

#the __str__ method prints the object    
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __rmul__(self, other):
        return Point(other * self.x, other * self.y) 

### Polymorphism - functions that take two types of datum
def multadd(x,y,z):
        return x * y + z

p = Point(1,0)
print p 

p1 = Point(3,4)
p2 = Point(5,7)
p3 = p1 + p2
print p3
print p1*p2
print 2 * p2
print multadd(p1, p2, 2)
print multadd(2, p1, p2)
