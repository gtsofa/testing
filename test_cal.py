# test calculator.py

import unittest

import cal

class TestCalc(unittest.TestCase):

    def test_add(self):
        """Test add function"""
        #result = cal.add(10,5)
        self.assertEqual(cal.add(10,5), 15)

if __name__=="__main__":
    unittest.main()