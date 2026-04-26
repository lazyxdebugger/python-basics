import re
def url_checker(url):
    try:
        pattern=r'^(https?\/\/)?(www\.)?[a-zA-Z0-9\.]+\.[a-zA-Z]{2,}(\/\/s*)?$'
        if re.match(pattern,url):
            print(f"{url} is valid")
            return
        else:
            raise ValueError("invalid url!")
    except ValueError as e:#go 4 spaces back if cannot allign properly
        print(e)
     
url=input("enter the url:")
url_checker(url)
