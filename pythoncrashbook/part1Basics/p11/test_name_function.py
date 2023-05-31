#A Passing Test

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'Janis 'Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')#the assert method verifies that a result we received matches the result we expected to receive and to check if is true we use a unittest assertEqual() method and pass it the string and there are compairing formatted_name and to know if there are equal otherwise let me know

    #Adding New Tests

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozert' work?"""
        formatted_name = get_formatted_name(
                'wolfgang','mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

