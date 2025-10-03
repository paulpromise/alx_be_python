class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def student_info(self):
        return f"{self.name} with ID of {self.id} and he is {self.age} years old"

class New_Student(Student):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)
        
    


studen1 = Student("Promise", 22, 20251001)



print(studen1.student_info())
