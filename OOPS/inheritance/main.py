# Parent class
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)


# child class
# V- 1 with pass - means child has not any property of it's own.
# class Student(Person):
#   pass

# v-2 child has its own property but using the parent's property
# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)


# v-3 -- using super() function to do the above job

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)


# v-4 -- with his own property which is exceptional from it's parent

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear = 2019

# creating object with child class
# x = Student("Mike", "Olsen")
# x.printname()
# print(x.graduationyear)


# Next 


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year


  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
# print(x.graduationyear)
x.welcome()
