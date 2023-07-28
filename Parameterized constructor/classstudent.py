'''Class object constructor attributes'''


class Student:

  def __init__(self, name, id):
    self.name=name #instance varibale
    self.id=id



s1=Student("Bob", 11)
s2=Student("Carol", 12)

print(s1.name, s1.id)
print(s2.name)
print(s2.id)
s2.id=33
print(s2.id)