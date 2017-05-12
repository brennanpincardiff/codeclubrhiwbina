from class_teacher import Teacher
from class_address import Address

address = Address()
address.address_line_1 = "Teacher Address Line 1"
address.address_line_2 = "Teacher Address Line 2"
address.address_line_3 = "Teacher Address Line 3"
address.address_line_4 = "Teacher Address Line 4"
address.postcode = "Teacher CF14 sdsad"

teacher = Teacher(1,"Miss Teacher Teacher",26,2,address.display())
print(teacher.display())
