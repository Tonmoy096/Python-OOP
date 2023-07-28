'''CLass object constructor methods '''

class Student:

    def __init__(self,name, id):
        self.name=name #instance variable
        self.id=id #instance variable

    def details(self): #instance method
        print("Name:",self.name,"ID:",self.id)

s1=Student("Bob",11)
s2=Student("Tonmoy",12)
s1.id=24
s1.details()

