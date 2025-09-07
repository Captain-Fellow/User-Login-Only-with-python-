from PasswordMatch import PasswordMatch

class User:
    def __init__(self, userName, password):
        self._userName = userName
        
        '''if PasswordMatch.is_strong(password):
            self._password = PasswordMatch(password)
            print("New User Added.")
        else:
            print("Error Creating new user...")
            raise ValueError("Password is not strong enough..")
        '''
        try:
            self._password = PasswordMatch(password)  # password is a string here
            print("New User added")
        except ValueError as e:
            print("Error Creating new user:", e)
            raise  # Re-raise the exception so the main loop can catch it

    @property
    def userName(self):
        return self._userName

    @property
    def password(self):
        return self._password
    
    @property
    def show_userName(self):
        print(f"Your User Name is: {self._userName}")

    @userName.setter
    def userName(self, value):
        self._userName = value
        print("UserName has been updated as : ", value) 

    @password.setter
    def password(self, value):
        print("Updating password...: Your Password must be strong")
        print("It must contain at least 8 characters, including uppercase, lowercase letters, and digits.")
        self._password = value
        print("Password has been updated.")



users = []

#userName_str= input("Enter Your User Name: ")
#password_str= input("Enter Your Password: ")
#new_user = User(userName_str, password_str)
#users.append(new_user)

user_choice = input("Want to add new user? (yes/no) : ").lower()

while user_choice != "no" and user_choice != "yes":
    print("Invalid input. Please enter 'yes' or 'no'.")
    user_choice = input("Want to add new user? (yes/no) : ").lower()

if user_choice == "yes":
    while True:
        userName_str = input("Enter Your User Name: ")
        password_str = input("Enter Your Password: ")
        try:
            new_user = User(userName_str, password_str)
            users.append(new_user)
            break  # Exit loop if successful
        except Exception as e:
            print("Enter correct username and password.")
else :
    print("No new user added.Tell me what you want to do next...  ")


'''
if input("Want to add another user? (yes/no)").lower() == "yes":
        userName = input("Enter Your User Name: ")
        password = PasswordMatch(input("Enter Your Password: "))
        new_user = User(userName, password)
        users.append(new_user)
'''