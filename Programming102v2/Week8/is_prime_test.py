import unittest
from is_prime import is_prime


class TestIsPrimeTest(unittest.TestCase):
    "This is a test class for testing is_prime funciton"
    
    def TestCase0(self):
        self.assertEqual(is_prime(7), "7 should noot be prime")

    def TestCase1(self):
        self.assertEqual(is_prime(8), "8 should be prime")


if __name__ == '__main__':
    unittest.main()
    