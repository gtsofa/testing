# test calculator.py

import unittest

import cal

class TestCalc(unittest.TestCase):

    def test_add(self):
        """Test add function"""
        #result = cal.add(10,5)
        self.assertEqual(cal.add(10,5), 15)#hcases
        self.assertEqual(cal.add(-1,1), 0)
        self.assertEqual(cal.add(-1,-1), -2)

    def test_subtract(self):
        """Test add function"""
        #result = cal.add(10,5)
        self.assertEqual(cal.subtract(10,5), 5)#hcases
        self.assertEqual(cal.subtract(-1,1), -2)
        self.assertEqual(cal.subtract(-1,-1), 0)

    def test_multiply(self):
        """Test add function"""
        #result = cal.add(10,5)
        self.assertEqual(cal.multiply(10,5), 50)#hcases
        self.assertEqual(cal.multiply(-1,1), -1)
        self.assertEqual(cal.multiply(-1,-1), 1)

    def test_divide(self):
        """Test add function"""
        #result = cal.add(10,5)
        self.assertEqual(cal.divide(10,5), 2)#hcases
        self.assertEqual(cal.divide(-1,1), -1)
        self.assertEqual(cal.divide(-1,-1), 1)

        #self.assertRaises(ValueError, cal.divide, 10, 2)#3 args -exception we expect,fun we r testing,arguments for the functio
        #using the contextmanager
        with self.assertRaises(ValueError):
            cal.divide(10, 0)

if __name__=="__main__":
    unittest.main()