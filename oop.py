class Student:
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

    def display(self):
     print(self.first_name, self.last_name)
my_student=Student(first_name="John", last_name="Carson")
my_student.display()
my_student1=Student(first_name="Jack", last_name="Siso")
my_student1.display()
my_student2=Student(first_name="Melvin", last_name="Agnes")
my_student2.display()
my_student3=Student(first_name="Victoria", last_name="Shanon")
my_student3.display()
my_student4=Student(first_name="Samson", last_name="Oremo")
my_student4.display()