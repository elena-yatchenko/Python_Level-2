import pytest
from HW_14_Employee import Employee, Person


@pytest.fixture
def emp():
    print("created employee")
    return Employee("ivanov", "ivan", "ivanovich", 30, "manager", 50000)


def test_employee_full_name(emp):
    assert emp.full_name() == "Ivanov Ivan Ivanovich"


def test_employee_birthday(emp):
    emp.birthday()
    assert emp.get_age() == 31


def test_employee_raise_salary(emp):
    emp.raise_salary(10)
    assert emp.salary == 55000.0


def test_employee_str(emp):
    assert str(emp) == "Ivanov Ivan Ivanovich (Manager)"


def test_employee_last_name_title(emp):
    assert emp.last_name == "Ivanov"


if __name__ == "__main__":
    pytest.main(["-v"])

# HW_14_pytest_6.py .....                                                                                            [100%]

"""если закомментить мою корректировку с round(округлением до 1 знака после запятой)"""
# HW_14_pytest_6.py ..F..                                                                                            [100%]