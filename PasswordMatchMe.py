class PasswordMatch:
    def __init__(self, password):
        if self.is_strong(password):
            self._password = password
            print("Password is strong.")
        else:
            print("Password is not strong enough. It must contain at least 8 characters, including uppercase, lowercase letters, and digits.")
            raise ValueError("Password is not strong enough.")

    @staticmethod
    def is_strong(value):
        return (
            len(value) >= 8 and
            any(c.isupper() for c in value) and
            any(c.islower() for c in value) and
            any(c.isdigit() for c in value)
        )

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if self.is_strong(value):
            self._password = value
            print("Password is strong.")
        else:
            print("Password is not strong enough. It must contain at least 8 characters, including uppercase, lowercase letters, and digits.")
            raise ValueError("Password is not strong enough.")