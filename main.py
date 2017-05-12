import tkinter as tk
from class_address import Address
from class_school import School
from class_student import Student
from class_teacher import Teacher
from class_course import Course
from tkinter import *
from tkinter import ttk

school = object;
course = object;
teacher = object;
student = object;

class Demo1( Frame ):
    def __init__( self ):
        self.addSchool()


    def new_window(self):
        self.newWindow = Demo1()



    def createAddressFeilds(self,row):
        self.address_line1_label = Label(self, text="Address Line 1").grid(row=row)
        self.address_line1_input = Entry(self).grid(row=row, column=1)
        row = row+1
        self.address_line2_label = Label(self, text="Address Line 2").grid(row=row)
        self.address_line2_input = Entry(self).grid(row=row, column=1)
        row = row+1
        self.address_line3_label = Label(self, text="Address Line 3").grid(row=row)
        self.address_line3_input = Entry(self).grid(row=row, column=1)
        row = row+1
        self.address_line4_label = Label(self, text="Address Line 4").grid(row=row)
        self.address_line4_input = Entry(self).grid(row=row, column=1)
        row = row+1
        self.postcode_label = Label(self, text="Postcode").grid(row=row)
        self.postcode_input = Entry(self).grid(row=row, column=1)
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
        self.pack();
        self.mainloop()

    def addCourse(self):
        tk.Frame.__init__(self)
        self.master.title("Add Course")
        self.course_id_label = Label(self, text="Course Id").grid(row=0)
        self.course_id_input = Entry(self).grid(row=0, column=1)
        self.course_name_label = Label(self, text="Course Name").grid(row=1)
        self.course_name_input = Entry(self).grid(row=1, column=1)
        self.course_length_label = Label(self, text="Course Length").grid(row=2)
        self.course_length_input = Entry(self).grid(row=2, column=1)
        self.fail_grade_label = Label(self, text="Fail Grade").grid(row=3)
        self.fail_grade_input = Entry(self).grid(row=3, column=1)
        self.pass_grade_label = Label(self, text="Pass Grade").grid(row=4)
        self.pass_grade_input = Entry(self).grid(row=4, column=1)
        self.pack();
        self.mainloop()

    def addStudent(self):
        self.master.title("Add Student")
        self.student_id_label = Label(self, text="Student Id").grid(row=0)
        self.student_id_input = Entry(self).grid(row=0, column=1)
        self.student_name_label = Label(self, text="Student Name").grid(row=1)
        self.student_name_input = Entry(self).grid(row=1, column=1)
        self.student_age_label = Label(self, text="Student Age").grid(row=2)
        self.student_age_input = Entry(self).grid(row=2, column=1)
        row = self.createAddressFeilds(3)

    def addTeacher(self):
        self.master.title("Add Teacher")
        self.teacher_id_label = Label(self, text="Teacher Id").grid(row=0)
        self.teacher_id_input = Entry(self).grid(row=0, column=1)
        self.teacher_name_label = Label(self, text="Teacher Name").grid(row=1)
        self.teacher_name_input = Entry(self).grid(row=1, column=1)
        self.teacher_age_label = Label(self, text="Teacher Age").grid(row=2)
        self.teacher_age_input = Entry(self).grid(row=2, column=1)
        self.years_of_service_label = Label(self, text="Years of Service").grid(row=3)
        self.years_of_service_input = Entry(self).grid(row=3, column=1)
        row = self.createAddressFeilds(4)

    def createSchool(self):
        print(self.school_id_input.get());
        self.pack_forget()
        self.grid_forget()
        self.addCourse()

def main():
    Demo1()

if __name__ == '__main__':
    main()