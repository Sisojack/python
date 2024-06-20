class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
    def print_name(self):
        print(f'My name is {self.first_name }{self.last_name} and I am {self.age}years old')

class Student(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

myStudent=Student('Jack ','Siso','35 ')
myStudent.print_name()
myStudent1=Student('Melvin ','Agnes','20 ')
myStudent1.print_name()
myStudent2=Student('Jack ','Bruno','21 ')
myStudent2.print_name()
myStudent3=Student('Patience ','Waeni','19 ')
myStudent3.print_name()