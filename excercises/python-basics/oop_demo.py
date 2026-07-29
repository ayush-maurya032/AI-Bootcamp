class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

    def __str__(self):
        return f"Student(name = {self.name}, age = {self.age})"

student1 = Student("Ayush", 25)
student2 = Student("Rahul", 22)

student1.introduce()
student2.introduce()
print(student1)