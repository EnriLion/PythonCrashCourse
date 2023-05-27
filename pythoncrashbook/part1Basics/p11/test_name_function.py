#Unit Tests and Test Cases
##The module unittest(Standar libary); provides tools for testing your code. A unit test (verify that one specific aspect of a function's behavior is correct) and a test case(collection of unit test that together prove that a function behaves as is'ts supposed to.
#A test case with "full coverage" includes test to represent each of these situations also the possible ways you can use a function.
#Achieveing full coverage on a large project can be daunting(write test is often good to our critical behaviors and then aim for full coverage if the project starts to see widespread use.

#A Passing Test

#We need to impor thte unittest module and the function we want to test and then create a class that inherits from unittest.TestCase, and write a series of methods to test different aspects of your function's behavior.

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):#we create a class called NamesTestCase(contains a series of unit test for get_formatted_name())
    """Test for 'name_function.py'"""

    def test_first_last_name(self):
        """Test for 'name_function.py'"""
        fromatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(fromatted_name, 'Janis Jopin')

if __name__ == '_main_':
    unittest.main()

