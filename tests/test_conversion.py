import os, sys
sys.path.append(os.getcwd())

import source.conversion
import unittest

class TestConversion(unittest.TestCase):
    def test_latitude(self):
        self.assertEqual(source.conversion.convert("20000000")[0], 20.00)

    def test_longitude_greater_than_100(self):
        self.assertEqual(source.conversion.convert("00001000")[1], -110.00)

    def test_longitude_less_than_or_equal_100(self):
        self.assertEqual(source.conversion.convert("00009000")[1], -90.00)

    def test_continue_coordinate(self):
        self.assertEqual(source.conversion.convert("99999999"), (99.99,-99.99))



if __name__=='__main__':
    unittest.main()
