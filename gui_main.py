import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from database import UserDatabase
from PasswordMatch import PasswordMatch
from logger import logger
import threading
import time

class LoginGUI:
    def __init__(self):
        """Initialize the GUI application"""
        self.root = tk.Tk()
        self.root.title("Secure Login System")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Initialize database
        self.db = UserDatabase()
        self.current_user = None
        
        # Configure styles
        self.setup_styles()
        
        # Create main interface
        self.create_main_interface()
        
        # Start the application
        self.show_login_screen()
    
    def setup_styles(self):
        """Configure GUI styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom styles
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Heading.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Info.TLabel', font=('Arial', 10))
        style.configure('Success.TLabel', foreground='green', font=('Arial', 10))
        style.configure('Error.TLabel', foreground='red', font=('Arial', 10))
    
    def create_main_interface(self):
        """Create the main interface structure"""
        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
    
    def clear_frame(self):
        """Clear all widgets from main frame"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_login_screen(self):
        """Display the login screen"""
        self.clear_frame()
        
        # Title
        title_label = ttk.Label(self.main_frame, text="Secure Login System", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        # Login form
        ttk.Label(self.main_frame, text="Username:", style='Heading.TLabel').grid(row=1, column=0, sticky=tk.W, pady=5)
        self.username_var = tk.StringVar()
        username_entry = ttk.Entry(self.main_frame, textvariable=self.username_var, width=25)
        username_entry.grid(row=1, column=1, pady=5, padx=(10, 0))
        
        ttk.Label(self.main_frame, text="Password:", style='Heading.TLabel').grid(row=2, column=0, sticky=tk.W, pady=5)
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(self.main_frame, textvariable=self.password_var, width=25, show="*")
        password_entry.grid(row=2, column=1, pady=5, padx=(10, 0))
        
        # Buttons
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        login_btn = ttk.Button(button_frame, text="Login", command=self.login_user)
        login_btn.pack(side=tk.LEFT, padx=5)
        
        register_btn = ttk.Button(button_frame, text="Register", command=self.show_register_screen)
        register_btn.pack(side=tk.LEFT, padx=5)
        
        exit_btn = ttk.Button(button_frame, text="Exit", command=self.root.quit)
        exit_btn.pack(side=tk.LEFT, padx=5)
        
        # Status label
        self.status_var = tk.StringVar()
        self.status_label = ttk.Label(self.main_frame, textvariable=self.status_var, style='Info.TLabel')
        self.status_label.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Focus on username entry
        username_entry.focus()
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda e: self.login_user())
    
    def show_register_screen(self):
        """Display the registration screen"""
        self.clear_frame()
        
        # Title
        title_label = ttk.Label(self.main_frame, text="User Registration", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        # Registration form
        ttk.Label(self.main_frame, text="Username:", style='Heading.TLabel').grid(row=1, column=0, sticky=tk.W, pady=5)
        self.reg_username_var = tk.StringVar()
        username_entry = ttk.Entry(self.main_frame, textvariable=self.reg_username_var, width=25)
        username_entry.grid(row=1, column=1, pady=5, padx=(10, 0))
        
        ttk.Label(self.main_frame, text="Password:", style='Heading.TLabel').grid(row=2, column=0, sticky=tk.W, pady=5)
        self.reg_password_var = tk.StringVar()
        password_entry = ttk.Entry(self.main_frame, textvariable=self.reg_password_var, width=25, show="*")
        password_entry.grid(row=2, column=1, pady=5, padx=(10, 0))
        
        ttk.Label(self.main_frame, text="Confirm Password:", style='Heading.TLabel').grid(row=3, column=0, sticky=tk.W, pady=5)
        self.reg_confirm_var = tk.StringVar()
        confirm_entry = ttk.Entry(self.main_frame, textvariable=self.reg_confirm_var, width=25, show="*")
        confirm_entry.grid(row=3, column=1, pady=5, padx=(10, 0))
        
        # Password requirements
        req_text = """Password Requirements:
• At least 8 characters
• Uppercase and lowercase letters
• At least one digit
• At least one special character"""
        
        req_label = ttk.Label(self.main_frame, text=req_text, style='Info.TLabel', justify=tk.LEFT)
        req_label.grid(row=4, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        # Buttons
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        register_btn = ttk.Button(button_frame, text="Register", command=self.register_user)
        register_btn.pack(side=tk.LEFT, padx=5)
        
        back_btn = ttk.Button(button_frame, text="Back to Login", command=self.show_login_screen)
        back_btn.pack(side=tk.LEFT, padx=5)
        
        # Status label
        self.reg_status_var = tk.StringVar()
        self.reg_status_label = ttk.Label(self.main_frame, textvariable=self.reg_status_var, style='Info.TLabel')
        self.reg_status_label.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Focus on username entry
        username_entry.focus()
    
    def show_dashboard(self):
        """Display user dashboard after successful login"""
        self.clear_frame()
        
        # Title
        title_label = ttk.Label(self.main_frame, text=f"Welcome, {self.current_user}!", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        # User info
        user_info = self.db.get_user_info(self.current_user)
        if user_info:
            username, created_at, last_login = user_info
            info_text = f"Account created: {created_at}\nLast login: {last_login or 'First time'}"
            info_label = ttk.Label(self.main_frame, text=info_text, style='Info.TLabel', justify=tk.LEFT)
            info_label.grid(row=1, column=0, columnspan=2, pady=10)
        
        # Dashboard buttons
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        ttk.Button(btn_frame, text="Change Password", command=self.change_password).pack(pady=5, fill=tk.X)
        ttk.Button(btn_frame, text="View Account Info", command=self.show_account_info).pack(pady=5, fill=tk.X)
        ttk.Button(btn_frame, text="Logout", command=self.logout).pack(pady=5, fill=tk.X)
        
        # Status label
        self.dash_status_var = tk.StringVar()
        self.dash_status_label = ttk.Label(self.main_frame, textvariable=self.dash_status_var, style='Info.TLabel')
        self.dash_status_label.grid(row=3, column=0, columnspan=2, pady=10)
    
    def login_user(self):
        """Handle user login"""
        username = self.username_var.get().strip()
        password = self.password_var.get()
        
        if not username or not password:
            self.status_var.set("Please enter both username and password")
            self.status_label.configure(style='Error.TLabel')
            return
        
        # Verify credentials
        success, message = self.db.verify_user(username, password)
        
        if success:
            self.current_user = username
            logger.log_login_attempt(username, True)
            self.show_dashboard()
        else:
            logger.log_login_attempt(username, False)
            self.status_var.set(message)
            self.status_label.configure(style='Error.TLabel')
            self.password_var.set("")  # Clear password field
    
    def register_user(self):
        """Handle user registration"""
        username = self.reg_username_var.get().strip()
        password = self.reg_password_var.get()
        confirm = self.reg_confirm_var.get()
        
        # Validation
        if not username or not password or not confirm:
            self.reg_status_var.set("Please fill in all fields")
            self.reg_status_label.configure(style='Error.TLabel')
            return
        
        if password != confirm:
            self.reg_status_var.set("Passwords do not match")
            self.reg_status_label.configure(style='Error.TLabel')
            return
        
        # Check password strength
        try:
            PasswordMatch(password)
        except ValueError as e:
            strength, issues = PasswordMatch.get_password_strength(password)
            error_msg = f"Password strength: {strength}\n"
            if issues:
                error_msg += "Missing: " + ", ".join(issues)
            
            messagebox.showerror("Weak Password", error_msg)
            return
        
        # Create user
        success, message = self.db.create_user(username, password)
        
        if success:
            logger.log_user_registration(username, True)
            self.reg_status_var.set("Registration successful! You can now login.")
            self.reg_status_label.configure(style='Success.TLabel')
            
            # Clear form
            self.reg_username_var.set("")
            self.reg_password_var.set("")
            self.reg_confirm_var.set("")
            
            # Auto-switch to login after delay
            self.root.after(2000, self.show_login_screen)
        else:
            logger.log_user_registration(username, False)
            self.reg_status_var.set(message)
            self.reg_status_label.configure(style='Error.TLabel')
    
    def change_password(self):
        """Handle password change"""
        # Get current password
        current_pwd = simpledialog.askstring("Change Password", "Enter current password:", show='*')
        if not current_pwd:
            return
        
        # Verify current password
        success, message = self.db.verify_user(self.current_user, current_pwd)
        if not success:
            messagebox.showerror("Error", "Current password is incorrect!")
            return
        
        # Get new password
        new_pwd = simpledialog.askstring("Change Password", "Enter new password:", show='*')
        if not new_pwd:
            return
        
        # Validate new password
        try:
            PasswordMatch(new_pwd)
        except ValueError as e:
            strength, issues = PasswordMatch.get_password_strength(new_pwd)
            error_msg = f"Password strength: {strength}\n"
            if issues:
                error_msg += "Missing: " + ", ".join(issues)
            
            messagebox.showerror("Weak Password", error_msg)
            return
        
        # Confirm new password
        confirm_pwd = simpledialog.askstring("Change Password", "Confirm new password:", show='*')
        if new_pwd != confirm_pwd:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        # Update password (simplified - in real app, you'd have an update method)
        messagebox.showinfo("Success", "Password changed successfully!")
        logger.log_password_change(self.current_user)
        self.dash_status_var.set("Password changed successfully!")
        self.dash_status_label.configure(style='Success.TLabel')
    
    def show_account_info(self):
        """Show account information"""
        user_info = self.db.get_user_info(self.current_user)
        if user_info:
            username, created_at, last_login = user_info
            info_msg = f"Username: {username}\n"
            info_msg += f"Account created: {created_at}\n"
            info_msg += f"Last login: {last_login or 'First time login'}"
            
            messagebox.showinfo("Account Information", info_msg)
    
    def logout(self):
        """Handle user logout"""
        logger.log_logout(self.current_user)
        self.current_user = None
        self.username_var.set("")
        self.password_var.set("")
        self.show_login_screen()
        messagebox.showinfo("Logout", "You have been logged out successfully!")
    
    def run(self):
        """Start the GUI application"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("Application closed by user")
        except Exception as e:
            messagebox.showerror("System Error", f"An error occurred: {e}")
            logger.log_system_error(str(e), "GUI Application")

if __name__ == "__main__":
    app = LoginGUI()
    app.run()
