class Cat:
    def __init__(self,name,action):
        self.name=name
        self.action=action

    def view(self):
        print(self.name,self.action)
    
    def compare(self,ct):
        if self.action==ct.action:
            print("Bothe cat are", ct.action )
        else:
            print("They are different")

c1=Cat("mewao","Jumping")
c2=Cat("Luma","Sitting")

c1.view()
c2.view()

c1.compare(c2)

        