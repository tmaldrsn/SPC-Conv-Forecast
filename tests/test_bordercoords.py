import os, sys
sys.path.append(os.getcwd())

import source.bordercoords
import unittest


class TestInBoundaries(unittest.TestCase):
    def test_south(self):
        lat = 20 - 0.001
        lon = -100
        self.assertTrue(source.bordercoords.out_of_boundaries(lat, lon))

    def test_east(self):
        lat = 30
        lon = -125 - 0.001
        self.assertTrue(source.bordercoords.out_of_boundaries(lat, lon))

    def test_west(self):
        lat = 30
        lon = 10 + 0.001
        self.assertTrue(source.bordercoords.out_of_boundaries(lat, lon))


if __name__=='__main__':
    unittest.main()
