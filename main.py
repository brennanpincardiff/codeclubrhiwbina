import tkinter as tk
from class_address import Address
from class_school import School
from class_student import Student
from class_teacher import Teacher
from class_course import Course
from tkinter import *
from tkinter import ttk



class Demo1( Frame ):
    school = object
    course = object
    teacher = object
    student = object

    def __init__( self ):
        self.addSchool()


    def new_window(self):
        self.newWindow = Demo1()



    def createAddressFeilds(self,row):
        self.address_line1_label = Label(self, text="Address Line 1").grid(row=row)
        self.address_line1_input = StringVar()
        Entry(self,textvariable=self.address_line1_input).grid(row=row, column=1)
        row = row+1
        self.address_line2_label = Label(self, text="Address Line 2").grid(row=row)
        self.address_line2_input = StringVar()
        Entry(self,textvariable=self.address_line2_input).grid(row=row, column=1)
        row = row+1
        self.address_line3_label = Label(self, text="Address Line 3").grid(row=row)
        self.address_line3_input = StringVar()
        Entry(self,textvariable=self.address_line3_input).grid(row=row, column=1)
        row = row+1
        self.address_line4_label = Label(self, text="Address Line 4").grid(row=row)
        self.address_line4_input = StringVar()
        Entry(self,textvariable=self.address_line4_input).grid(row=row, column=1)
        row = row+1
        self.postcode_label = Label(self, text="Postcode").grid(row=row)
        self.postcode_input = StringVar()
        Entry(self,textvariable=self.postcode_input).grid(row=row, column=1)
        row = row + 1
        return row

    def addSchool(self):
        tk.Frame.__init__(self)
        self.master.title("Add School")
        self.school_id_label = Label(self, text="School Id").grid(row=0)
        self.school_id_input = StringVar()
        Entry(self, textvariable=self.school_id_input).grid(row=0, column=1)
        self.school_name_label = Label(self, text="School Name").grid(row=1)
        self.school_name_input = StringVar()
        Entry(self, textvariable=self.school_name_input).grid(row=1, column=1)
        self.founded_label = Label(self, text="Founded").grid(row=2)
        self.founded_input = StringVar()
        Entry(self, textvariable=self.founded_input).grid(row=2, column=1)
        self.motto_label = Label(self, text="Motto").grid(row=3)
        self.motto_input = StringVar()
        Entry(self, textvariable=self.motto_input).grid(row=3, column=1)
        row = self.createAddressFeilds(4)
        self.button_school = Button(self,text ="OK",command = self.createSchool).grid(row=row)
        self.pack()
        self.mainloop()

    def createSchool(self):
        address = Address()
        address.address_line_1 = self.address_line1_input.get()
        address.address_line_2 = self.address_line2_input.get()
        address.address_line_3 = self.address_line3_input.get()
        address.address_line_4 = self.address_line4_input.get()
        address.postcode = self.postcode_input.get()

        self.school = School(self.school_id_input.get(), self.school_name_input.get(),self.founded_input.get(),self.motto_input.get(),address.display())
        errors = self.school.checkErrors()
        if len(errors) > 0:
            print(errors)
        else:

            self.pack_forget()
            self.grid_forget()
            self.addCourse()

    def createCourse(self):
        self.course = Course(self.course_id_input.get(),self.course_name_input.get(),self.course_length_input.get(),self.fail_grade_input.get(),self.pass_grade_input.get())
        errors = self.course.checkErrors()
        if len(errors) > 0:
            print(errors)
        else:
            self.pack_forget()
            self.grid_forget()
            self.addTeacher()


    def addCourse(self):
        tk.Frame.__init__(self)
        self.master.title("Add Course")
        self.course_id_label = Label(self, text="Course Id").grid(row=0)
        self.course_id_input = StringVar()
        Entry(self, textvariable=self.course_id_input).grid(row=0, column=1)
        self.course_name_label = Label(self, text="Course Name").grid(row=1)
        self.course_name_input = StringVar()
        Entry(self, textvariable=self.course_name_input).grid(row=1, column=1)
        self.course_length_label = Label(self, text="Course Length").grid(row=2)
        self.course_length_input = StringVar()
        Entry(self,textvariable=self.course_length_input).grid(row=2, column=1)
        self.fail_grade_label = Label(self, text="Fail Grade").grid(row=3)
        self.fail_grade_input = StringVar()
        Entry(self,textvariable=self.fail_grade_input).grid(row=3, column=1)
        self.pass_grade_label = Label(self, text="Pass Grade").grid(row=4)
        self.pass_grade_input = StringVar()
        Entry(self,textvariable=self.pass_grade_input).grid(row=4, column=1)
        self.button_course = Button(self,text ="OK",command = self.createCourse).grid(row=5)
        self.pack()
        self.mainloop()

    def createStudent(self):
        address = Address()
        address.address_line_1 = self.address_line1_input.get()
        address.address_line_2 = self.address_line2_input.get()
        address.address_line_3 = self.address_line3_input.get()
        address.address_line_4 = self.address_line4_input.get()
        address.postcode = self.postcode_input.get()
        self.student = Student(self.student_id_input.get(),self.student_name_input.get(),self.student_age_input.get(),address.display())
        errors = self.student.checkErrors()
        if len(errors) > 0:
            print(errors)
        else:
           self.pack_forget()
           self.grid_forget()
           self.displayEnd()

    def addStudent(self):
        tk.Frame.__init__(self)
        self.master.title("Add Student")
        self.student_id_label = Label(self, text="Student Id").grid(row=0)
        self.student_id_input = StringVar()
        Entry(self, textvariable=self.student_id_input).grid(row=0, column=1)
        self.student_name_label = Label(self, text="Student Name").grid(row=1)
        self.student_name_input = StringVar()
        Entry(self, textvariable=self.student_name_input).grid(row=1, column=1)
        self.student_age_label = Label(self, text="Student Age").grid(row=2)
        self.student_age_input = StringVar()
        Entry(self, textvariable=self.student_age_input).grid(row=2, column=1)
        row = self.createAddressFeilds(3)
        self.button_course = Button(self, text="OK", command=self.createStudent).grid(row=row)
        self.pack()
        self.mainloop()

    def createTeacher(self):
        address = Address()
        address.address_line_1 = self.address_line1_input.get()
        address.address_line_2 = self.address_line2_input.get()
        address.address_line_3 = self.address_line3_input.get()
        address.address_line_4 = self.address_line4_input.get()
        address.postcode = self.postcode_input.get()
        self.teacher = Teacher(self.teacher_id_input.get(),self.teacher_name_input.get(),self.teacher_age_input.get(),self.years_of_service_input.get(),address.display())
        errors = self.teacher.checkErrors()
        if len(errors) > 0:
            print(errors)
        else:
            self.pack_forget()
            self.grid_forget()
            self.addStudent()


    def addTeacher(self):
        tk.Frame.__init__(self)
        self.master.title("Add Teacher")
        self.teacher_id_label = Label(self, text="Teacher Id").grid(row=0)
        self.teacher_id_input = StringVar()
        Entry(self,textvariable=self.teacher_id_input).grid(row=0, column=1)
        self.teacher_name_label = Label(self, text="Teacher Name").grid(row=1)
        self.teacher_name_input = StringVar()
        Entry(self,textvariable=self.teacher_name_input).grid(row=1, column=1)
        self.teacher_age_label = Label(self, text="Teacher Age").grid(row=2)
        self.teacher_age_input = StringVar()
        Entry(self,textvariable=self.teacher_age_input).grid(row=2, column=1)
        self.years_of_service_label = Label(self, text="Years of Service").grid(row=3)
        self.years_of_service_input = StringVar()
        Entry(self,textvariable=self.years_of_service_input).grid(row=3, column=1)
        row = self.createAddressFeilds(4)
        self.button_course = Button(self, text="OK", command=self.createTeacher).grid(row=row)
        self.pack()
        self.mainloop()

    def displayEnd(self):
        tk.Frame.__init__(self)
        self.master.title("Results")
        self.school_label = Label(self, text="School").grid(row=0)
        self.school_val = Label(self, text=self.school.display()).grid(row=1)
        self.course_label = Label(self, text="Course").grid(row=2)
        self.course_val = Label(self, text=self.course.display()).grid(row=3)
        self.teacher_label = Label(self, text="Teacher").grid(row=4)
        self.teacher_val = Label(self, text=self.teacher.display()).grid(row=5)
        self.student_label = Label(self, text="Student").grid(row=6)
        self.student_val = Label(self, text=self.student.display()).grid(row=7)
        self.pack();
        self.mainloop()


def main():
    Demo1()

if __name__ == '__main__':
    main()