import sqlite3
import hashlib
from datetime import datetime

class UserDatabase:
    def __init__(self, db_name="users.db"):
        """Initialize database connection and create tables if they don't exist"""
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Create the users table if it doesn't exist"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_login TIMESTAMP
                )
            ''')
            conn.commit()
    
    def hash_password(self, password):
        """Hash password using SHA-256 for security"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def create_user(self, username, password):
        """Create a new user in the database"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                password_hash = self.hash_password(password)
                cursor.execute(
                    "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                    (username, password_hash)
                )
                conn.commit()
                return True, "User created successfully!"
        except sqlite3.IntegrityError:
            return False, "Username already exists!"
        except Exception as e:
            return False, f"Error creating user: {str(e)}"
    
    def verify_user(self, username, password):
        """Verify user credentials"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                password_hash = self.hash_password(password)
                cursor.execute(
                    "SELECT id FROM users WHERE username = ? AND password_hash = ?",
                    (username, password_hash)
                )
                result = cursor.fetchone()
                
                if result:
                    # Update last login time
                    cursor.execute(
                        "UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE username = ?",
                        (username,)
                    )
                    conn.commit()
                    return True, "Login successful!"
                else:
                    return False, "Invalid username or password!"
        except Exception as e:
            return False, f"Error during login: {str(e)}"
    
    def user_exists(self, username):
        """Check if username already exists"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
            return cursor.fetchone() is not None
    
    def get_user_info(self, username):
        """Get user information"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT username, created_at, last_login FROM users WHERE username = ?",
                (username,)
            )
            return cursor.fetchone()
