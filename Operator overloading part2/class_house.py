class House:

    def __init__(self, w, d):
        self.window = w
        self.door = d

    def view(self):
        print("The house has", self.window, "windows and", self.door, "Door")

    def __add__(self, other):
        new_window = self.window+other.window
        new_door = self.door+other.door
        return new_window, new_door


h1 = House(6, 5)
h2 = House(7, 6)
h1.view()
h2.view()
print(h1+h2)
