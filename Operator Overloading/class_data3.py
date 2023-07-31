class data:

    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if self.x == other.x:
            print("bothe are equal")
        else:
            print("Not equal xD")


num1 = data(10)
num2 = data(10)
num1 == num2
