import unittest
import timeit
a=900
def factorial(a):
    if type(a)!=str:
        k=1
        if  a>0 and type(a)==int:
            for i in range(1,a+1):
                k=k*i
            return k
        else:
            if a==0 and type(a)==int :
                return 1
            else:
                try:
                    p=1/0
                except:
                    print('Введенное значение не принадлежит множеству целых неотрицательных чисел')
    if type(a)==str:
        try:
            p=1/0
        except:
            print('Введенное значение не принадлежит множеству целых неотрицательных чисел')
        



print(timeit.timeit("factorial(a)", setup="from __main__ import factorial,a", number=1))
class Test_Factorial(unittest.TestCase):
    def test_one(self):
        self.assertEqual(factorial(1),1)
    def test_zero(self):
        self.assertEqual(factorial(0),1)
    def test_Natural(self):
        self.assertEqual(factorial(5),120)
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(4),24)
        
if __name__=='__main__':
    unittest.main()

