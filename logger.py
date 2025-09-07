import logging
import os
from datetime import datetime
from config import LOG_FILE, LOG_LEVEL, ENABLE_LOGGING

class SystemLogger:
    def __init__(self):
        """Initialize the logging system"""
        if ENABLE_LOGGING:
            self.setup_logger()
    
    def setup_logger(self):
        """Configure the logger"""
        # Create logs directory if it doesn't exist
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # Configure logging
        log_path = os.path.join(log_dir, LOG_FILE)
        
        logging.basicConfig(
            level=getattr(logging, LOG_LEVEL),
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path),
                logging.StreamHandler()  # Also log to console
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("Login system started")
    
    def log_user_registration(self, username, success=True):
        """Log user registration attempts"""
        if ENABLE_LOGGING:
            if success:
                self.logger.info(f"User registration successful: {username}")
            else:
                self.logger.warning(f"User registration failed: {username}")
    
    def log_login_attempt(self, username, success=True, ip_address=None):
        """Log login attempts"""
        if ENABLE_LOGGING:
            ip_info = f" from {ip_address}" if ip_address else ""
            if success:
                self.logger.info(f"Login successful: {username}{ip_info}")
            else:
                self.logger.warning(f"Login failed: {username}{ip_info}")
    
    def log_logout(self, username):
        """Log user logout"""
        if ENABLE_LOGGING:
            self.logger.info(f"User logout: {username}")
    
    def log_password_change(self, username):
        """Log password changes"""
        if ENABLE_LOGGING:
            self.logger.info(f"Password changed: {username}")
    
    def log_security_event(self, event, username=None, details=None):
        """Log security-related events"""
        if ENABLE_LOGGING:
            message = f"Security event: {event}"
            if username:
                message += f" - User: {username}"
            if details:
                message += f" - Details: {details}"
            self.logger.warning(message)
    
    def log_system_error(self, error, context=None):
        """Log system errors"""
        if ENABLE_LOGGING:
            message = f"System error: {error}"
            if context:
                message += f" - Context: {context}"
            self.logger.error(message)
    
    def log_database_operation(self, operation, success=True, details=None):
        """Log database operations"""
        if ENABLE_LOGGING:
            status = "successful" if success else "failed"
            message = f"Database {operation} {status}"
            if details:
                message += f" - {details}"
            
            if success:
                self.logger.info(message)
            else:
                self.logger.error(message)

# Global logger instance
logger = SystemLogger()
