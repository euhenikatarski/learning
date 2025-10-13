import pytest
from Employee_class import Employee

@pytest.fixture
def employee():
    emp = Employee('oleg', 'shmal', 1500)
    return emp


def test_give_default_raise(employee):
    #emp = Employee('oleg', 'shmal', 1500)
    employee.give_raise()
    assert employee.money == 6500


def test_give_custom_raise(employee):
    #emp = Employee('oleg', 'shmal', 1500)
    employee.give_raise(1000)
    assert employee.money == 2500