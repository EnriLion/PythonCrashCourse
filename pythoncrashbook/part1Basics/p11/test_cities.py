import unittest
from city_functions import get_formatted_country

class NamesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Do names like 'Santiago 'Chile' work?"""
        formatted_place = get_formatted_country('santiago', 'chile')
        self.assertEqual(formatted_place, 'Santiago Chile')

if __name__ == '__main__':
    unittest.main()
