class Calculator:

    def product(self, *num):  # here the * will give you a tuple
        prod = 1
        for x in num:
            prod = prod*x
        print(prod)


c1 = Calculator()
c1.product(4, 5, 6, 7)
c1.product(70, 2)
