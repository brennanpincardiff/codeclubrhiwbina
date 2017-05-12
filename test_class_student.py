from class_student import Student
from class_address import Address

address = Address()
address.address_line_1 = "Address Line 1"
address.address_line_2 = "Address Line 2"
address.address_line_3 = "Address Line 3"
address.address_line_4 = "Address Line 4"
address.postcode = "CF14 sdsad"

student = Student(1,"Gareth Gwyther",100,address.display())
student_result = student.display()
print(student_result)