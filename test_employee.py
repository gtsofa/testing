# test employee class

import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):

    # DRY
    def setUp(self):
        """will run before any single test"""
        self.emp_1 = Employee('Tsofa', 'Nyule', 50000)
        self.emp_2 = Employee('Kitsao', 'Baya', 60000)

    def tearDown(self):
        """will run after any single test"""

        pass

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'John.Doe@email.com')
        self.assertEqual(self.emp_2.email, 'Tsofa.Nyule@email.com')

        emp_1.first = 'Julius'
        emp_2.first = 'Samuel'

        self.assertEqual(self.emp_1.email, 'Julius.Nyule@email.com')
        self.assertEqual(self.emp_2.email, 'Samuel.Baya@email.com')

    def test_fullname(self):

        self.assertEqual(self.emp_1.fullname, 'Julius Nyule')
        self.assertEqual(self.emp_2.fullname, 'Samuel Baya')

        self.emp_1.first = 'Julius'
        self.emp_2.first = 'Samuel'

        self.assertEqual(self.emp_1.fullname, 'Julis Doe')
        self.assertEqual(self.emp_2.fullname, 'Samuel Nyule')

    def test_apply_raise(self):
        #check the apply raise funct

        emp_1.apply_raise()
        emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 546000)
        self.assertEqual(self.emp_2.pay, 735000)

if __name__=='__main__':
    unittest.main()

