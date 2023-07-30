class Student:

    def __init__(self, **info):
        if len(info) == 3:
            self.name = info["name"]
            self.id = info["id"]
            self.CGPA = info["CG"]
        elif len(info) == 2:
            self.name = info["name"]
            self.id = info["id"]
        elif len(info) == 1:
            self.name = info["name"]

        print("Student info created")

    def display(self):
        if hasattr(self, "CGPA"):
            print(f"{self.name}, {self.id}, {self.CGPA}")
        else:
            print(self.name, self.id)


s1 = Student(name="Tonmoy", id="12", CG=3.5)
s2 = Student(name="Tuki", id="11")
s1.display()
s2.display()
