from multipledispatch import dispatch


class my_calculator:

    @dispatch(int, int)
    def product(self, a, b):
        print(a*b)

    @dispatch(int, int, int)
    def product(self, a, b, c):
        print(a*b*c)

    @dispatch(float, int)
    def product(self, a, b):
        print(a*b)

    @dispatch(float, float, float)
    def product(self, a, b, c):
        print(a*b*c)

    @dispatch(str, int)
    def product(self, a, b):
        print(int(a)*b)


c1 = my_calculator()
c1.product(4, 5, 3)
c1.product("4", 2)
c1.product(4.5, 2)
