class Student:
    student_id = 0
    name = ""
    age = 0
    address = ""

    def __init__(self,student_id,name, age,address):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.address = address

    def checkErrors(self):
        return ""

    def display(self):
        return str(self.student_id)+" "+self.name+" "+str(self.age)+" "+str(self.address)
