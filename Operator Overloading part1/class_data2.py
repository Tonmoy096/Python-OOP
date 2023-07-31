class data:

    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        if self.x < other.x:
            return "num1 is less than num2"
        else:
            return "num2 is less than num1"


num1 = data(10)
num2 = data(20)
print(num1 < num2)
