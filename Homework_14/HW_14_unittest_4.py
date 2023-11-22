from HW_14_Employee import Employee, Person
import unittest

"""используем setUp, который сам создает пользователя для каждого метода, поэтому используем self для
экземпляра класса (хотя на практике вроде работает и без него)"""

class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.emp = Employee("ivanov", "ivan", "ivanovich", 30, "manager", 50000)

    def test_employee_full_name(self):
        self.assertEqual(self.emp.full_name(), "Ivanov Ivan Ivanovich")

    def test_employee_birthday(self):
        self.emp.birthday()
        self.assertEqual(self.emp.get_age(), 31)

    def test_employee_raise_salary(self):
        self.emp.raise_salary(10)
        self.assertEqual(self.emp.salary, 55000.0)

    def test_employee_str(self):
        self.assertEqual(str(self.emp), "Ivanov Ivan Ivanovich (Manager)")

    def test_employee_last_name_title(self):
        self.assertEqual(self.emp.last_name, "Ivanov")


if __name__ == "__main__":
    unittest.main(verbosity=2)

# test_employee_birthday (__main__.TestEmployee.test_employee_birthday) ... ok
# test_employee_full_name (__main__.TestEmployee.test_employee_full_name) ... ok
# test_employee_last_name_title (__main__.TestEmployee.test_employee_last_name_title) ... ok
# test_employee_raise_salary (__main__.TestEmployee.test_employee_raise_salary) ... ok
# test_employee_str (__main__.TestEmployee.test_employee_str) ... ok

# ----------------------------------------------------------------------
# Ran 5 tests in 0.003s

# OK


"""если закомментить мою корректировку с round(округлением до 1 знака после запятой)"""
# FAILED (failures=1)
