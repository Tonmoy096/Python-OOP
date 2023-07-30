class data:

    def __init__(self, x):
        self.x = x

    def __gt__(self, other):
        if (self.x > other.x):
            return True
        else:
            return False


num1 = data(10)
num2 = data(20)
print(num1 > num2)
