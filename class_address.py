class Address:
    address_line_1 = ""
    address_line_2 = ""
    address_line_3 = ""
    address_line_4 = ""
    postcode = ""

    def checkErrors(self):
        return ""

    def display(self):
        return self.address_line_1+" "+self.address_line_2+" "+self.address_line_3+" "+self.address_line_4+" "+self.postcode
