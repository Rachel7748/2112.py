class Customer:
    def __init__(self, id, fname, lname, address, mobile_number):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.mobile_number = mobile_number

    def __repr__(self):
        return f'Customer({self.id},{self.fname},{self.lname},{self.address},{self.mobile_number})'
    def __str__(self):
        return f'id:{self.id},first name: {self.fname}, last name: {self.lname}, address: {self.address}, phone number: {self.mobile_number}'

 





