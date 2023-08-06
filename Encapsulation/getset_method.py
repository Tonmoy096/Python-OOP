class Student:

    def __init__(self, name, id):
        self.name = name
        self.__id = id  # private instance variable

    def details(self):
        print("Name:", self.name, "ID:", self.__id)

    def set_ID(self, id):  # we can update private varibale using this method
        if (id > 0):
            self.__id = id
        else:
            print("Invalid id, Please print agaio")

    def get_ID(self):  # we can get the value by using get methor
        return self.__id


s1 = Student("Tonmoy", 70)
s2 = Student("Jenat", 77)

s1.details()
s2.details()

s2.set_ID(71)
s2.details()
