import unittest
from population_functions import get_formatted_country

class NamesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Do names like 'Santiago 'Chile' work?"""
        formatted_place = get_formatted_country('santiago', 'chile')
        self.assertEqual(formatted_place, 'Santiago Chile')

    def test_city_country_population(self):
        """Do string like 'Santiago Chile - Population=500000' work?"""
        formatted_place = get_formatted_country(
                'santiago','chile', 'population=500000')
        self.assertEqual(formatted_place, 'Santiago Chile - Population=500000')

if __name__ == '__main__':
    unittest.main()
