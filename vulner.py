class vulnerability:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"vulnerability name:{self.name}"

v=vulnerability("SQL INJECTION")

setattr(v,"severity","HIGH")
setattr(v,"cvss_value",9.8)

print(v)#print using str()

print("printing info using attributes dynamically:")
print("vulnerability name:",getattr(v,"name"))
print("severity:",getattr(v,"severity"))
print("cvss_value:",getattr(v,"cvss_value"))

if hasattr(v,"exploit_available"):
    print("exploit_available exists")
    exit()
else:
    print("exploit_available does not exist")
