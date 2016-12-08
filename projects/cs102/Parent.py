class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def showInfo(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, cape_color):
        print ("Child Constructor called")
        Parent.__init__(self, last_name, eye_color) #this Constructor for classParent is how the Child inherits the parent instance variables
        self.cape_color = cape_color #this is where we declare the new attribute for the Child

    def showInfo(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("Cape Color - "+self.cape_color)

jor_el = Parent("El", "Green")
##
##print (jor_el.last_name)
##
kal_el = Child("El", "Green", "Red")
##print (kal_el.last_name)
##print (kal_el.cape_color)

##jor_el.showInfo()
##print("____")
kal_el.showInfo()
