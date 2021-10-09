from temperature import Temperature
import unittest

class TestTemperature(unittest.TestCase):

    def test_input_none(self):
        self.assertRaises(ValueError, Temperature)

    def test_input_multiple(self):
        args = (1,1)
        self.assertRaises(ValueError, Temperature, *args)

    def test_input_negative(self):
        self.assertRaises(ValueError, Temperature, -1)

    def test_input_celsius(self):
        self.assertEqual(Temperature(celsius=1).kelvin, 274.15)

    def test_input_fahrenheit(self):
        self.assertEqual(Temperature(fahrenheit=1).kelvin, (1 - 32) * 5 / 9 + 273.15)

    def test_input_kelvin(self):
        self.assertEqual(Temperature(1).kelvin, 1)
