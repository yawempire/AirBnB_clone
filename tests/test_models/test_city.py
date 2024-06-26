#!/usr/bin/python3
"""
Test for city class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    The test for the class method
    """
    def setUp(self):
        """
        Initializaing the object instance
        """
        city = City()

    def test_attributes(self):
        """
        Tests the various attribute types
        """
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_default_values(self):
        """
        Test the default values of this attribute
        """
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attribute_instance(self):
        """
        Test attribute instances
        """
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)


if __name__ == '__main__':
    unittest.main()
