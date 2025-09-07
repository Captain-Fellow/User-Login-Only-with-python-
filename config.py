# Configuration file for the login system

# Database settings
DATABASE_NAME = "users.db"

# Security settings
MIN_PASSWORD_LENGTH = 8
MAX_LOGIN_ATTEMPTS = 3
REQUIRE_SPECIAL_CHARS = True
REQUIRE_NUMBERS = True
REQUIRE_UPPERCASE = True
REQUIRE_LOWERCASE = True

# Session settings
SESSION_TIMEOUT_MINUTES = 30
AUTO_LOGOUT_WARNING_MINUTES = 5

# System messages
MESSAGES = {
    "welcome": "Welcome to the Secure Login System!",
    "goodbye": "Thank you for using our system. Goodbye!",
    "access_denied": "Access denied. Maximum login attempts exceeded.",
    "session_expired": "Your session has expired. Please login again.",
    "registration_success": "Registration successful! You can now login.",
    "login_success": "Login successful! Welcome back.",
    "password_changed": "Password changed successfully!",
    "invalid_credentials": "Invalid username or password.",
    "username_exists": "Username already exists. Please choose another.",
    "passwords_no_match": "Passwords do not match. Please try again.",
    "weak_password": "Password does not meet security requirements.",
}

# Console formatting
HEADER_WIDTH = 50
SEPARATOR = "=" * HEADER_WIDTH

# Logging settings
LOG_FILE = "system.log"
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# Feature flags
ENABLE_LOGGING = True
ENABLE_PASSWORD_HISTORY = False  # Prevent reusing last N passwords
ENABLE_ACCOUNT_LOCKOUT = True    # Lock account after failed attempts
ENABLE_PASSWORD_EXPIRY = False   # Force password change after N days
