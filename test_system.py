#!/usr/bin/env python3
"""
Simple test script for the login system components
"""

def test_password_validation():
    """Test password validation"""
    print("Testing password validation...")
    
    from PasswordMatch import PasswordMatch
    
    # Test weak passwords
    weak_passwords = ["123", "password", "Password", "Password123"]
    
    for pwd in weak_passwords:
        try:
            PasswordMatch(pwd)
            print(f"❌ '{pwd}' should have failed but passed")
        except ValueError:
            print(f"✅ '{pwd}' correctly rejected")
    
    # Test strong password
    try:
        PasswordMatch("MyP@ssw0rd123")
        print("✅ 'MyP@ssw0rd123' correctly accepted")
    except ValueError:
        print("❌ 'MyP@ssw0rd123' should have passed but failed")

def test_database():
    """Test database operations"""
    print("\nTesting database operations...")
    
    from database import UserDatabase
    import os
    
    # Use test database
    test_db = "test_users.db"
    if os.path.exists(test_db):
        os.remove(test_db)
    
    db = UserDatabase(test_db)
    
    # Test user creation
    success, message = db.create_user("testuser", "TestP@ss123")
    if success:
        print("✅ User creation successful")
    else:
        print(f"❌ User creation failed: {message}")
    
    # Test duplicate user
    success, message = db.create_user("testuser", "TestP@ss123")
    if not success and "already exists" in message:
        print("✅ Duplicate user correctly rejected")
    else:
        print(f"❌ Duplicate user should have been rejected: {message}")
    
    # Test login
    success, message = db.verify_user("testuser", "TestP@ss123")
    if success:
        print("✅ User login successful")
    else:
        print(f"❌ User login failed: {message}")
    
    # Test wrong password
    success, message = db.verify_user("testuser", "wrongpassword")
    if not success:
        print("✅ Wrong password correctly rejected")
    else:
        print("❌ Wrong password should have been rejected")
    
    # Cleanup
    if os.path.exists(test_db):
        os.remove(test_db)

def test_logger():
    """Test logging system"""
    print("\nTesting logging system...")
    
    try:
        from logger import logger
        logger.log_user_registration("testuser", True)
        logger.log_login_attempt("testuser", True)
        logger.log_logout("testuser")
        print("✅ Logging system working")
    except Exception as e:
        print(f"❌ Logging system failed: {e}")

if __name__ == "__main__":
    print("🔧 Running Login System Tests\n")
    
    try:
        test_password_validation()
        test_database()
        test_logger()
        
        print("\n✅ All tests completed!")
        print("\n🚀 You can now run 'python main.py' to start the login system")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        print("Please check your code and try again.")
