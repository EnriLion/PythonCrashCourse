import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the module employee"""
    def test_give_default_raise(self):
        """Test that gives the default result for salary"""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 105000)


    def test_give_custom_raise(self):
        """Test that gives a custom raise for salary"""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 110000)


    def setUp(self):
        """
        Create a  new employee in each test method
        """
        self.employee = Employee("Enrique", "Leon", 100000)

if __name__ == '__main__':
    unittest.main()
