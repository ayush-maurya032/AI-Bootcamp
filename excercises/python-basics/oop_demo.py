class Student:
    def __init__(self,name,age): #constructor
        self.name = name
        self.age = age

    def introduce(self):
        print(self)

student1 = Student("Ayush", 25)
student2 = Student("Rahul", 22)

student1.introduce()
student2.introduce()

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)