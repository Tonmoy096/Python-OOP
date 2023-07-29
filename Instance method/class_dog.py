class Dog:

    def __init__(self,name, color):
        self.name=name
        self.color=color

    def update_color(self,color):
        self.color=color

    def view(self):
        print("Name:",self.name,"Color:",self.color)

d1=Dog("Husky","Black")
d2=Dog("Tumba","Red")
d1.view()
d1.update_color("White")

d1.view()
d2.view()

print(d1.__dict__)