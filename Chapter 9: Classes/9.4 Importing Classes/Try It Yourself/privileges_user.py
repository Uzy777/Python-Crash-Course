class User:
    def __init__(self, first_name, last_name, age, sex, ethnicity, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.ethnicity = ethnicity
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nUser information:")
        print(f"firstname = {self.first_name}")
        print(f"lastname = {self.last_name}")
        print(f"age = {self.age}")
        print(f"sex = {self.sex}")
        print(f"ethnicity = {self.ethnicity}")
        print(f"login attempts = {self.login_attempts}")


    def greet_user(self):
        print(f"\nHello {self.first_name} {self.last_name} how are you doing today?")

    
    def increment_login_attempts(self):
        """Increase by +1 each time"""
        self.login_attempts += 1


    def reset_login_attempts(self):
        """Reset login_attempts to 0"""
        self.login_attempts = 0