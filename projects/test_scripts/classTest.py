# class Test():
#     def __init__(self):
#         self.toast = "bread"

#     def add(self,a,b):
#         print a + b

# Test()
# test = Test()
# print test.toast
# test.add(2,2)

# class Test2():
#     def __init__(self):
#         self.bread = "toast"
    
#     def add2(self, a):
#         print a*2

class Dog():
    def __init__(self):
        self.tail = "tail"
        self.hair = "fur"
        self.voice = "bark"
    
    def desc(self, a):
        print "Daisy was a dog who " + a

daisy = Dog()
print daisy.hair
daisy.desc("loved eating fallen avocados.")