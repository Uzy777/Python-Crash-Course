# 9-3. Users:   Make a class called User. Create two attributes called first_name and last_name, and then create
#               several other attributes that are typically stored in a user profile. Make a method called describe_user()
#               that prints a summary of the user's information. Make another method called greet_user() that prints
#               a personalised greeting to the user.
#               Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self, first_name, last_name, age, sex, ethnicity):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.ethnicity = ethnicity

    def describe_user(self):
        print(f"\nUser information:")
        print(f"firstname = {self.first_name}")
        print(f"lastname = {self.last_name}")
        print(f"age = {self.age}")
        print(f"sex = {self.sex}")
        print(f"ethnicity = {self.ethnicity}")


    def greet_user(self):
        print(f"\nHello {self.first_name} {self.last_name} how are you doing today?")


user_1 = User('James', 'Wallace', 24, 'Male', 'Chinese')
user_2 = User('Laura', 'Brim', 29, 'Female', 'British')
user_3 = User('Cale', 'Nameickle', 74, 'Male', 'Asian')


user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()