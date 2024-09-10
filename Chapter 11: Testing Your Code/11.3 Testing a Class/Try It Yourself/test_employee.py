from employee_3 import Employee

def test_give_default_raise():
    """Test the default raise of £5,000."""
    emp = Employee('John', 'Doe', 50000)  # Create an employee with a salary of £50,000
    emp.give_raise()  # Apply the default raise of £5,000
    assert emp.salary == 55000, f"Expected salary to be £55,000, but got {emp.salary}"



def test_give_custom_raise():
    """Test a custom raise amount."""
    emp = Employee('John', 'Doe', 50000)  # Create an employee with a salary of £50,000
    emp.give_raise(10000)  # Apply a custom raise of £10,000
    assert emp.salary == 60000, f"Expected salary to be £60,000, but got {emp.salary}"



