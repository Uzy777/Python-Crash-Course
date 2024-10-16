from privileges_user import User

class Privileges:
    def __init__(self, privileges=None):
        """Initialize the privileges list. If none is provided, use a default list."""
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges



    def show_privileges(self):
        """Lists the administrator's set of privileges"""
        print(f"Privileges: {self.privileges}")


class Admin(User):
    """Initialise attributes of the parent class."""
    def __init__(self, first_name, last_name, age, sex, ethnicity, login_attempts):
        super().__init__(first_name, last_name, age, sex, ethnicity, login_attempts)
        self.privileges = Privileges()