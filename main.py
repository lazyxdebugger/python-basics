from employee import Employee

elist=[]
def add_employee():
    first_name=input("enter the first name:")
    last_name=input("enter the last name:")
    username=input("enter the username:")
    email=input("enter the email:")

    emp=Employee(first_name,last_name,username,email)
    elist.append(emp)
    print("employee added succesfully!")

def display_all():
    if not elist:
        print("employee database is currently empty!")
        return
    else:
        for e in elist:
            e.display()
        
def display_employee():
    uname=input("enter the username:")
    for e in elist:
        if uname==e.username:
            e.display()
            return
        
    print("employee doesnt exist.")


#def menu():        
while True:
    print("--employee database--")
    print("1.add employee")
    print("2.display all employee")
    print("3.display employee details")
    print("4.exit")
    ch=int(input("enter ur choice:"))
    match ch:
        case 1:
            add_employee()
        case 2:
            display_all()
        case 3:
            display_employee()
        case 4:
            exit()
        case _:
            print("enter a valid choice:")
