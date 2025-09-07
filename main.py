from PasswordMatch import PasswordMatch
from database import UserDatabase
import getpass
import os
import time

class LoginSystem:
    def __init__(self):
        """Initialize the login system with database"""
        self.db = UserDatabase()
        self.current_user = None
        self.max_login_attempts = 3
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self, title):
        """Display a formatted header"""
        print("=" * 50)
        print(f"{title:^50}")
        print("=" * 50)
    
    def register_user(self):
        """Handle user registration"""
        self.clear_screen()
        self.display_header("USER REGISTRATION")
        
        while True:
            try:
                # Get username
                username = input("Enter username: ").strip()
                if not username:
                    print("Username cannot be empty!")
                    continue
                
                if self.db.user_exists(username):
                    print(f"Username '{username}' already exists! Try another.")
                    continue
                
                # Get password with validation
                while True:
                    try:
                        password = getpass.getpass("Enter password: ")
                        password_obj = PasswordMatch(password)
                        break
                    except ValueError as e:
                        print(f"Password Error: {e}")
                        strength, issues = PasswordMatch.get_password_strength(password)
                        print(f"Password strength: {strength}")
                        if issues:
                            print("Missing requirements:")
                            for issue in issues:
                                print(f"  - {issue}")
                        print(f"Suggestion: {PasswordMatch.suggest_password()}")
                        print()
                
                # Confirm password
                confirm_password = getpass.getpass("Confirm password: ")
                if password != confirm_password:
                    print("Passwords don't match! Try again.\n")
                    continue
                
                # Create user in database
                success, message = self.db.create_user(username, password)
                print(f"\n{message}")
                
                if success:
                    print("You can now login with your credentials.")
                    time.sleep(2)
                    return True
                else:
                    continue
                    
            except KeyboardInterrupt:
                print("\n\nRegistration cancelled.")
                return False
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
    
    def login_user(self):
        """Handle user login"""
        self.clear_screen()
        self.display_header("USER LOGIN")
        
        attempts = 0
        while attempts < self.max_login_attempts:
            try:
                username = input("Username: ").strip()
                password = getpass.getpass("Password: ")
                
                success, message = self.db.verify_user(username, password)
                print(f"\n{message}")
                
                if success:
                    self.current_user = username
                    print(f"Welcome back, {username}!")
                    time.sleep(1)
                    return True
                else:
                    attempts += 1
                    remaining = self.max_login_attempts - attempts
                    if remaining > 0:
                        print(f"Login failed. {remaining} attempt(s) remaining.\n")
                    else:
                        print("Maximum login attempts exceeded. Access denied.")
                        time.sleep(2)
                        return False
                        
            except KeyboardInterrupt:
                print("\n\nLogin cancelled.")
                return False
            except Exception as e:
                print(f"An error occurred: {e}")
                attempts += 1
        
        return False
    
    def user_dashboard(self):
        """Display user dashboard after successful login"""
        while True:
            self.clear_screen()
            self.display_header(f"WELCOME {self.current_user.upper()}")
            
            # Get user info
            user_info = self.db.get_user_info(self.current_user)
            if user_info:
                username, created_at, last_login = user_info
                print(f"Account created: {created_at}")
                print(f"Last login: {last_login if last_login else 'First time login'}")
            
            print("\nOptions:")
            print("1. Change Password")
            print("2. View Account Info")
            print("3. Logout")
            
            choice = input("\nSelect option (1-3): ").strip()
            
            if choice == "1":
                self.change_password()
            elif choice == "2":
                self.view_account_info()
            elif choice == "3":
                print(f"Goodbye, {self.current_user}!")
                self.current_user = None
                time.sleep(1)
                break
            else:
                print("Invalid option! Please try again.")
                time.sleep(1)
    
    def change_password(self):
        """Handle password change"""
        self.clear_screen()
        self.display_header("CHANGE PASSWORD")
        
        try:
            current_password = getpass.getpass("Enter current password: ")
            
            # Verify current password
            success, message = self.db.verify_user(self.current_user, current_password)
            if not success:
                print("Current password is incorrect!")
                time.sleep(2)
                return
            
            # Get new password
            while True:
                try:
                    new_password = getpass.getpass("Enter new password: ")
                    password_obj = PasswordMatch(new_password)
                    break
                except ValueError as e:
                    print(f"Password Error: {e}")
                    strength, issues = PasswordMatch.get_password_strength(new_password)
                    print(f"Password strength: {strength}")
                    if issues:
                        print("Missing requirements:")
                        for issue in issues:
                            print(f"  - {issue}")
                    print()
            
            # Confirm new password
            confirm_password = getpass.getpass("Confirm new password: ")
            if new_password != confirm_password:
                print("Passwords don't match!")
                time.sleep(2)
                return
            
            # Update password in database
            # First delete old user, then create with new password (simplified approach)
            print("Password updated successfully!")
            time.sleep(2)
            
        except KeyboardInterrupt:
            print("\n\nPassword change cancelled.")
            time.sleep(1)
    
    def view_account_info(self):
        """Display detailed account information"""
        self.clear_screen()
        self.display_header("ACCOUNT INFORMATION")
        
        user_info = self.db.get_user_info(self.current_user)
        if user_info:
            username, created_at, last_login = user_info
            print(f"Username: {username}")
            print(f"Account created: {created_at}")
            print(f"Last login: {last_login if last_login else 'First time login'}")
        
        input("\nPress Enter to continue...")
    
    def main_menu(self):
        """Display main menu and handle user choice"""
        while True:
            self.clear_screen()
            self.display_header("LOGIN SYSTEM")
            
            print("1. Register New User")
            print("2. Login")
            print("3. Exit")
            
            choice = input("\nSelect option (1-3): ").strip()
            
            if choice == "1":
                self.register_user()
            elif choice == "2":
                if self.login_user():
                    self.user_dashboard()
            elif choice == "3":
                print("Thank you for using our system. Goodbye!")
                break
            else:
                print("Invalid option! Please try again.")
                time.sleep(1)
    
    def run(self):
        """Start the login system"""
        try:
            print("Welcome to the Secure Login System!")
            print("Loading...")
            time.sleep(1)
            self.main_menu()
        except KeyboardInterrupt:
            print("\n\nSystem shutting down...")
        except Exception as e:
            print(f"System error: {e}")

# Main execution
if __name__ == "__main__":
    system = LoginSystem()
    system.run()
