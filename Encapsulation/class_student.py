class Student:
    def __init__(self, name, id):
        self.name = name  # instance variable
        self.__id = id  # private instance variable

    def view(self):
        print(self.name, self.__id)

    def update_id(self, id):
        if id > 0:
            self.__id = id
        else:
            print("invalid id, enter id again")


s1 = Student("Bob", 1240144)
s2 = Student("Lala", 7896)


s1.update_id(10)

s1.view()
s2.view()
