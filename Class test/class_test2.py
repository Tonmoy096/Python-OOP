class Basic_Calculator():
    def add(self, *numbers):
        sum=1
        for i in numbers:
            sum *= i
        return sum

calculator = Basic_Calculator()
user_input = input("Enter numbers separated by a space: ")
numbers = list(map(int, user_input.split()))
result = calculator.add(*numbers)
print(result)
