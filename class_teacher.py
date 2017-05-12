class Teacher:
    teacher_id = 0
    name = ""
    age = 0
    years_of_service = 0
    address = ""

    def __init__(self,teacher_id, name, age,years_of_service,address):
        self.teacher_id = teacher_id
        self.name = name
        self.age = age
        self.address = address
        self.years_of_service = years_of_service

    def checkErrors(self):
        return ""

    def display(self):
        return str(self.teacher_id)+" "+self.name + " " + str(self.age) + " "+ str(self.address) +" "+ str(self.years_of_service)
