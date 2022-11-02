# Object Oriented Programming Example
# Function: Creating new users

import datetime as dt
class Member:                               #Class name
    def __init__(self, uname, fname):       #Create object definitions
        self.username = uname               #Object atributes = values
        self.fullname = fname
        self.active = True
        self.join_date = dt.date.today()

# Creating object based on class        
new_guy = Member('GKrov', 'Gabriel Kasparov')

#Let's check on this new guy
print("New user's data: ")
print(f"Username: {new_guy.username}")
print(f"Fullname: {new_guy.fullname}")
print(f"Date Joined: {new_guy.join_date: %m/%d/%y}")
print(f"Status: {new_guy.active}")
print(f"Type: {type(new_guy)}")

print(f"Full Data: {new_guy}")