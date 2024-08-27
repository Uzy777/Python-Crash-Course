# 9-7. Admin:       An administrator is a special kind of user. Write a class called Admin that inherits from the user class you wrote in Exercise 9-3 or Exercise 9-5.
#                   Add an attribute 'privileges', that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
#                   Write a method called 'show_privileges()' that lists the administrator's set of privileges. Create an instance of 'Admin', and call your method.

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


class Admin(User):
    """Initialise attributes of the parent class."""
    def __init__(self, first_name, last_name, age, sex, ethnicity, login_attempts):
        super().__init__(first_name, last_name, age, sex, ethnicity, login_attempts)
        self.privileges = ["can add post", "can delete post", "can ban user"]


    def show_privileges(self):
        """Lists the administrator's set of privileges"""
        print(f"Privileges: {self.privileges}")


admin_1 = Admin('Tim', 'Lex', 37, 'Male', 'British', 0,)
admin_1.show_privileges()