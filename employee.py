class Employee:
    def __init__(self,first_name,last_name,username,email):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.email=email

    def display(self):
        print("--employee info--")
        print("first name:",self.first_name)
        print("last name:",self.last_name)
        print("username:",self.username)
        print("email:",self.email)
