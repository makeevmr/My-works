import unittest
from memory_profiler import profile
@profile
def factorial(a):
    if type(a)!=int:
        raise TypeError('Введенное значение не является целым числом')
    if a < 0:
        raise ValueError('Введенное значение явлется отрицательным числом')
    if a==0:
        return 1
    else:
        return factorial(a-1)*a

class Test_Factorial(unittest.TestCase):
    def test_one(self):
        self.assertEqual(factorial(1),1)
    def test_zero(self):
        self.assertEqual(factorial(0),1)
    def test_Natural(self):
        self.assertEqual(factorial(5),120)
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(4),24)
    def test_error_string(self):
        self.assertRaises(TypeError, factorial, 'lol')
        self.assertRaises(TypeError, factorial, '')
        self.assertRaises(TypeError, factorial, ' ')
    def test_error_neg(self):
        self.assertRaises(ValueError, factorial, -4)
        self.assertRaises(ValueError, factorial, -81)
      
if __name__=='__main__':
    unittest.main()
