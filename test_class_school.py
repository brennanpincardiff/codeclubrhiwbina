from class_school import School
from class_address import Address

address = Address()
address.address_line_1 = "Highlands of Scotland"
address.address_line_2 = "??"
address.address_line_3 = "??"
address.address_line_4 = "??"
address.postcode = "??"

school = School(1,"Hogwarts",10,'Draco dormiens nunquam titillandus',address.display())
school_result = school.display()
print(school_result)