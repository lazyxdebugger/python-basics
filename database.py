users={}

def add_user():
    username=input("enter the username:")
    if username in users:
        print(f"user {username} already exists")
        return
    else:
        password=input("enter the password:")
        if len(password)<6:
            print("password length be more than 6 characters")
            return
        else:
            users[username]=password
            print(f"user {username} added successfully!")

def update_password():
    username=input("enter the username to update the password:")
    if username not in users:
        print(f"given user {username} doesnt exist.")
        return
    else:
        new_pass=input("enter the new password:")
        users[username]=new_pass
        print("password updated successfully!")
     
def delete_password():
    username=input("enter the username to delete password:")
    if username not in users:
        print(f"user with username {username} doesnt exist.")
        return
    else:
        users[username]=None
        print("password deleted successfully!")
      
def delete_user():
    print("WARNING!THIS WILL PERMANENTLY DELETE THE USER.")
    username=input("enter the username:")
    if username not in users:
        print(f"{username} user doesnt exist.")
        return
    else:
        del users[username]
        print(f"user with username {username} deleted successfully!")
      
def search_user():
    username=input("enter the username to be searched:")
    if username in users:
        print("user is present in the database.")
        return
    else:
        print("user not found!")
        
def display_users():
    if not users:
        print("user database is currently empty.")
        return
    else:
        for i in users:
            print(i)

while True:
    print("--user database management system--")
    print("1.add user")
    print("2.update password")
    print("3.delete password")
    print("4.delete a user")
    print("5.search for a user")
    print("6.display all users")
    print("7.exit")
    ch=int(input("enter ur choice:"))
    match ch:
        case 1:
            add_user()
        case 2:
            update_password()
        case 3:
            delete_password()
        case 4:
            delete_user()
        case 5:
            search_user()
        case 6:
            display_users()
        case 7:
            exit()
        case '_':
            print("enter a correct choice!")



            
            
