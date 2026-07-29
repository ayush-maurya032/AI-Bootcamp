class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

    def __str__(self):
        return f"Student(name = {self.name}, age = {self.age})"

    def have_birthday(self):
         self.age += 1
 
    def change_name(self,new_name):
        self.name = new_name

student1 = Student("Ayush", 25)
student2 = Student("Rahul", 22)

student1.introduce()
student2.introduce()
student1.have_birthday()
print(student1)


print(student1)

student1.change_name("Amit")

print(student1)