import unittest
import sampletest

class ClassTest(unittest.TestCase):
    def test_add(self):
        print("this is add function")
        self.assertEqual(sampletest.add(10, 20), 30)
        self.assertEqual(sampletest.add(5, 5), 10)
        self.assertEqual(sampletest.add(-1, -1), -1)
        

    def test_sub(self):
        print("this is sub function")
        self.assertEqual(sampletest.sub(10, 20), -10)
        self.assertEqual(sampletest.sub(5, 5), 0)
        self.assertEqual(sampletest.sub(-1, -3), -2)

    def test_mul(self):
        print("this is mul function")
        self.assertEqual(sampletest.mul(10, 20), 200)
        self.assertEqual(sampletest.mul(5, 5), 25)
        self.assertEqual(sampletest.mul(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()


