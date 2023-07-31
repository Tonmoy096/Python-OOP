class data:

    def __init__(self, x):
        self.x = x

    # add method for two objects

    def __add__(self, other):
        print(self.x+other.x)  # we can also use return here


num1 = data(10)
num2 = data(40)
str1 = data("CSE")
str = data("111")
num1+num2
str1+str
