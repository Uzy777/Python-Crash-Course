import pytest
from employee_3 import Employee

@pytest.fixture
def employee():
    """Fixture that provides an Employee instance."""
    return Employee('John', 'Doe', 50000)  # Create an employee with a salary of £50,000

def test_give_default_raise(employee):
    """Test the default raise of £5,000."""
    employee.give_raise()  # Apply the default raise of £5,000
    assert employee.salary == 55000, f"Expected salary to be £55,000, but got {employee.salary}"

def test_give_custom_raise(employee):
    """Test a custom raise amount."""
    employee.give_raise(10000)  # Apply a custom raise of £10,000
    assert employee.salary == 60000, f"Expected salary to be £60,000, but got {employee.salary}"
