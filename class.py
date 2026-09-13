"""class car:
    pass


car1 = car()
car2 = car()


class Student:
     def __init__ (self, name, age):
          self.name = name
          self.age = age

Student1 = Student("Mehran", 29)
Student2 = Student("Ali", 25)

print(Student1.name, Student1.age)

"""



class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(self.name)
        print(self.age)

    def change_age(self, new_age):
        input_age = str(input("please enter new age "))
        return input_age


    Student1 = Student("Mehran", 29)

    