# User Login System - Built with Python

This repo contains a complete, industry-standard login system with strong password validation, built entirely using Python for learning purposes.

## 🚀 Features

### Core Features
- ✅ User Registration with strong password validation
- ✅ Secure Login with password hashing (SHA-256)
- ✅ SQLite database for persistent data storage
- ✅ Session management and user dashboard
- ✅ Password change functionality
- ✅ Comprehensive logging system
- ✅ Input validation and error handling
- ✅ Security features (max login attempts, account lockout)

### Security Features
- 🔐 Password hashing using SHA-256
- 🔐 Strong password requirements (8+ chars, uppercase, lowercase, digits, special chars)
- 🔐 Protection against SQL injection
- 🔐 Secure password input (hidden typing)
- 🔐 Login attempt limiting
- 🔐 Comprehensive audit logging

## 📁 Project Structure

```
Login-System/
│
├── main.py              # Main application entry point
├── database.py          # Database operations (SQLite)
├── PasswordMatch.py     # Password validation logic
├── logger.py           # Logging system
├── config.py           # Configuration settings
├── test_system.py      # Test suite
├── requirements.txt    # Dependencies (none needed!)
├── README.md          # This file
│
├── logs/              # Generated log files
│   └── system.log
│
└── users.db           # SQLite database (auto-created)
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No external packages needed! (Uses only Python standard library)

### Quick Start
1. Clone or download the project files
2. Open terminal in the project directory
3. Run the test suite: `python test_system.py`
4. Start the application: `python main.py`

## 📖 Usage Guide

### Registration
1. Select "Register New User" from main menu
2. Enter a unique username
3. Create a strong password (requirements will be shown if password is weak)
4. Confirm your password
5. Registration complete!

### Login
1. Select "Login" from main menu
2. Enter your username and password
3. Access your dashboard upon successful login

### User Dashboard
After login, you can:
- Change your password
- View account information
- Logout securely

## 🔧 Configuration

Edit `config.py` to customize:
- Password requirements
- Login attempt limits
- Logging settings
- Security features

## 🧪 Testing

Run the test suite:
```bash
python test_system.py
```

This tests:
- Password validation
- Database operations
- User registration/login
- Logging system

## 📝 Learning Concepts Covered

### Python Concepts
1. **Object-Oriented Programming (OOP)**
   - Classes and objects
   - Properties and methods
   - Encapsulation
   - Inheritance potential

2. **Exception Handling**
   - Try/except blocks
   - Custom exceptions
   - Error propagation
   - Graceful error handling

3. **Database Operations**
   - SQLite integration
   - SQL queries
   - Database schema design
   - Transaction management

4. **Security Concepts**
   - Password hashing
   - Input validation
   - SQL injection prevention
   - Secure coding practices

5. **File I/O & Logging**
   - File operations
   - Logging configuration
   - Log rotation concepts
   - Debugging techniques

6. **System Integration**
   - Configuration management
   - Modular design
   - Testing strategies
   - Documentation

### Industry Standards Applied
- **Security**: Password hashing, input validation, audit logging
- **Architecture**: Separation of concerns, modular design
- **Testing**: Unit tests, integration tests
- **Documentation**: README, code comments, configuration
- **Logging**: Structured logging, different log levels
- **Error Handling**: Graceful degradation, user-friendly messages

## 🔐 Security Considerations

### Current Implementation
- ✅ Password hashing (SHA-256)
- ✅ Input validation
- ✅ SQL injection prevention
- ✅ Login attempt limiting
- ✅ Secure password input
- ✅ Audit logging

### Production Enhancements (Advanced)
- Use bcrypt/scrypt/Argon2 instead of SHA-256
- Add salt to password hashing
- Implement session tokens
- Add HTTPS/TLS encryption
- Rate limiting by IP address
- Two-factor authentication (2FA)
- Password complexity scoring
- Account lockout policies

## 🚀 Next Steps for Learning

### Phase 1: Web Interface
- Learn Flask/Django
- Create HTML templates
- Add CSS styling
- Implement AJAX for dynamic updates

### Phase 2: Advanced Security
- Implement bcrypt for password hashing
- Add session management
- Learn about JWT tokens
- Implement 2FA

### Phase 3: Database Enhancement
- Learn PostgreSQL/MySQL
- Implement database migrations
- Add foreign key relationships
- Learn about database indexing

### Phase 4: Deployment
- Learn Docker containerization
- Deploy to cloud (AWS/Heroku)
- Set up CI/CD pipelines
- Monitor with logging services

## 📚 Additional Resources

### Python Learning
- [Python Official Documentation](https://docs.python.org/)
- [Real Python](https://realpython.com/)
- [Python Security](https://python-security.readthedocs.io/)

### Database Learning
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Database Design](https://www.lucidchart.com/pages/database-diagram/database-design)

### Security Learning
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python-security.readthedocs.io/)

## 🤝 Contributing

This is a learning project! Feel free to:
- Add new features
- Improve security
- Enhance the UI
- Add more tests
- Improve documentation

## 📄 License

This project is for educational purposes. Feel free to use and modify as needed for learning.

---

**Happy Coding! 🎉**

Remember: This project covers fundamental concepts. Keep learning and building upon these foundations to create more advanced applications!
