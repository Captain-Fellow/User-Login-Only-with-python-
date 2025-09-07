import re
import string

class PasswordMatch:
    def __init__(self, password):
        if self.is_strong(password):
            self._password = password
            print("Password is strong.")
        else:
            print("Password requirements not met.")
            raise ValueError("Password is not strong enough.")

    @staticmethod
    def is_strong(value):
        """Enhanced password validation with detailed requirements"""
        return (
            len(value) >= 8 and
            any(c.isupper() for c in value) and
            any(c.islower() for c in value) and
            any(c.isdigit() for c in value) and
            any(c in string.punctuation for c in value)  # Require special characters
        )
    
    @staticmethod
    def get_password_strength(password):
        """Return detailed password strength analysis"""
        issues = []
        
        if len(password) < 8:
            issues.append("At least 8 characters")
        if not any(c.isupper() for c in password):
            issues.append("At least one uppercase letter")
        if not any(c.islower() for c in password):
            issues.append("At least one lowercase letter")
        if not any(c.isdigit() for c in password):
            issues.append("At least one digit")
        if not any(c in string.punctuation for c in password):
            issues.append("At least one special character (!@#$%^&*)")
        
        if not issues:
            return "Strong", []
        elif len(issues) <= 2:
            return "Medium", issues
        else:
            return "Weak", issues
    
    @staticmethod
    def suggest_password():
        """Suggest a strong password format"""
        return "Example: MyP@ssw0rd123 (uppercase, lowercase, digits, special chars)"

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if self.is_strong(value):
            self._password = value
            print("Password is strong.")
        else:
            strength, issues = self.get_password_strength(value)
            print(f"Password strength: {strength}")
            print("Missing requirements:")
            for issue in issues:
                print(f"  - {issue}")
            print(f"Suggestion: {self.suggest_password()}")
            raise ValueError("Password is not strong enough.")