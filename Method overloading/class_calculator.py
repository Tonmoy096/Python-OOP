class Calculator:

    def product(self,*num):
        sum=1
        for x in num:
            sum=sum*x
        print(sum)

c1=Calculator()
c1.product(4,5,6,7)
c1.product(70,2)