
class user:
    name = 'Barbara Ann'
    email = 'barbara.ann@gmail.com'
    password = '12345678'
   

    def login(self):
        entry_name = input("Enter your name:")
        entry_email = input("Enter your email:")
        entry_password = input("Enter your password:")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(self.name))
        else:
            print("you are not authorized for this page.")
            

class employee(user):
        title = 'clerk'
        department = 'General'
        pin_number = '555'
        badge_id = '721'

        def login(self):
            entry_name = input("Enter your name:")
            entry_email = input("Enter your email:")
            entry_pin_number = input("Enter your pin:")
            if (entry_email == self.email and entry_pin_number == self.pin_number):
                print("You clocked in!".format(entry_pin_number))
            else:
                print("you are not authorized for this page.")
            

class customer(user):
        mailing_address = '123 maple street '
        mailing_list = True
        phone_number= ' '
        zipcode = ' '
        
customer= user()
customer.login()

employee1 = employee()
employee1.login()


