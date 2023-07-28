class House:
    def __init__(self):
        self.window=4
        self.door=3

    def view(self):
        print(self.window, self.door)

h1=House()
h1.view()
h2=House()
h2.view()