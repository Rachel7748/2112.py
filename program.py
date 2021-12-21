import sqlite3
from customer import Customer
from dataaccess import DataAccess

conn = sqlite3.connect('C:/racheli/proj3/proj3.db')
cur = conn.execute('SELECT * FROM customer')
cus1 = DataAccess('C:/racheli/proj3/proj3.db')

def menu():
    return f'1. Get all customers \n2. Get customer by id \n3. Insert customer \n4. Delete customer \n5. Update customer \n6. Exit \n please enter your choose'

def print_all_customers(self):
    self.cur.execute('SELECT * FROM CUSTOMER')
    for row in self.cur:
            print (Customer(row[0],row[1],row[2],row[3],row[4]))

def get_customer():
    id = int(input('enter id:'))
    Customer = cur.get_customer(id)
    print(Customer)

def insert(Customer):
    id = int(input('enter id:'))
    fname = str(input('enter first name:'))
    lname = str(input('enter last name:'))
    address = str(input('enter address:'))
    mobile_number = str(input('enter phone number:'))
    Customer = Customer(id, fname, lname, address, mobile_number)
    cur.insert_customer(Customer)
    print('records updated')

def delete(id):
    id = int(input('enter id:'))
    cur.delete_customer(id)
    print('records updated')


def update():
    id = int(input('enter current id:'))

    _id = int(input('enter new id:'))
    _fname = str(input('enter first name:'))
    _lname = str(input('enter last name:'))
    _address = str(input('enter address:'))
    _mobile_number = str(input('enter phone number:'))
    #Customer = customer(_id, _fname, _lname, _address, _mobile_number)
    cur.update_customer(id, Customer)
    print('records updated')


def select(choose_num):
    if choose_num == 1:
         print_all_customers(conn)
    elif choose_num == 2:
        return get_customer()
    elif choose_num == 3:
        return insert()
    elif choose_num == 4:
        return delete()
    elif choose_num == 5:
        return update()

def main():
    choose_num = int(input(f'\n{menu()}'))
    select(choose_num)
    return f'chosen number: {choose_num}'



#conn = ('C:/racheli/proj3/proj3.db')
main()
#conn = sqlite3.connect('C:/racheli/proj3/proj3.db').close()





