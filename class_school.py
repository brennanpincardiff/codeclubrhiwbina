class School:
    school_id = 0
    name = ""
    founded = ""
    motto = ""

    def __init__(self, school_id, name, founded,motto, address):
        self.school_id = school_id
        self.name = name
        self.founded = founded
        self.motto = motto
        self.address = address

    def checkErrors(self):
        return ""


    def display(self):
        return str(self.school_id) + " " + self.name + " " + str(self.founded) + " "+ str(self.motto) + " " + str(self.address)



