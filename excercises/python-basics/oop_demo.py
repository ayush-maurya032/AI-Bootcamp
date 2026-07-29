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
 
    def change_name(self, new_name):

         if new_name == "":
            raise ValueError("Name cannot be empty.")

         self.name = new_name

student1 = Student("Ayush", 25)
student2 = Student("Rahul", 22)




try:
    student1.change_name("")

except ValueError as e:
    print(e)
