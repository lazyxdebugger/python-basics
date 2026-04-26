class user:
    def __init__(self,username):
        self.username=username
    def login(self,password=None,otp=None):
        if password and otp:
            print(f"{self.username} logged in using 2FA.")
        elif password:
            print(f"{self.username} logged in using just password.")
        else:
            print("no credentials provided..cannot login.")
    def access_resource(self):
        print(f"{self.username} has basic access.")

           
class admin(user):
    def __init__(self,username):
        super().__init__(username)
    def access_resource(self):
        print(f"{self.username} has all access.")
    def delete_logs(self):
        print(f"{self.username} can delete logs.")


class guest(user):
    def __init__(self,username):
        super().__init__(username)
    def access_resource(self):
        print(f"{self.username} has limited access.")

a=admin("admin_user")
u=user("normal_user")
g=guest("guest_user")

a.access_resource()
u.access_resource()
g.access_resource()

a.login("admin@123",97887)
u.login("user@123")
g.login()
           
