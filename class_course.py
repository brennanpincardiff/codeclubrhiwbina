class Course:
    course_id = 0
    course_name = ""
    course_length = ""
    fail_grade = ""
    pass_grade = ""

    def __init__(self, course_id, course_name, course_length, fail_grade, pass_grade):
        self.course_id = course_id
        self.course_name = course_name
        self.course_length = course_length
        self.fail_grade = fail_grade
        self.pass_grade = pass_grade

    def checkErrors(self):
        return ""

    def display(self):
        return str(self.course_id)+" "+self.course_name+" "+str(self.course_length)+" "+str(self.fail_grade)+" "+str(self.pass_grade)
