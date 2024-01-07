# 9-5. Login Attempts:  Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162).
#                       Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
#                       Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
#                    
#                       Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts
#                       to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure
#                       it was reset to 0.



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


user_1 = User('James', 'Wallace', 24, 'Male', 'Chinese', 0)
user_2 = User('Laura', 'Brim', 29, 'Female', 'British', 0)
user_3 = User('Cale', 'Nameickle', 74, 'Male', 'Asian', 0)


user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.increment_login_attempts()
user_3.increment_login_attempts()
user_3.reset_login_attempts()   # Reset to 0
user_3.describe_user()
user_3.greet_user()
