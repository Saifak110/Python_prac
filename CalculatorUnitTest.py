import unittest
from Calculator import Calculator
class CalculatorUnitTest(unittest.TestCase):
    def test_add(self):
        cal = Calculator()
        self.assertEqual(cal.add(10, 20), 30)
        self.assertEqual(cal.add(5, 5), 10)
        self.assertEqual(cal.add(-1, -1), -2)
    
    def test_sub(self):
        print("this is sub function")
        cal = Calculator()
        self.assertEqual(cal.sub(10, 10), 0)
        self.assertEqual(cal.sub(10, 5), 5)
        self.assertEqual(cal.sub(1, 1), 0)

    def test_mul(self):
        print("this is mul function")
        cal = Calculator()
        self.assertEqual(cal.mul(10, 10), 100)
        self.assertEqual(cal.mul(10, 5), 50)
        self.assertEqual(cal.mul(1, 1), 1)
if __name__ == '__main__':
    unittest.main()
