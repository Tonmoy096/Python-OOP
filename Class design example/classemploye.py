class Emplopyee:
    #parameterized constructor
    def __init__(self,name,no):
        self.no=no  #instance variable[object varibale]
        self.name=name  #instance variable
    
    #instance method
    def display(self):
        print(self.name,self.no)

emp1=Emplopyee("John",11)  #instance 1
emp2=Emplopyee("David",12)  #instance 2
emp1.display()
emp2.display()