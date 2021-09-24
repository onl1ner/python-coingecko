import sys
sys.path.append('..')

import unittest
from src.main import get_coins

class TestCoins(unittest.TestCase):
    def test_10(self):
        self.assertEqual(len(get_coins(10)), 10)
    
    def test_321(self):
        self.assertEqual(len(get_coins(321)), 321)
    
    def test_string(self):
        self.assertEqual(len(get_coins('string')), 0)
    
    def test_negative(self):
        self.assertEqual(len(get_coins(-1)), 0)
    
    pass

if __name__ == '__main__':
    unittest.main()