from math import factorial
from unittest import TestCase, main
def line(m):
    lst=[]
    for i in range(m+1):
        C=int((factorial(m)/(factorial(m-i)*factorial(i))))
        lst.append(C)
    return lst
def Pascal_trianngle(n):
    if type(n)!=int:
        raise TypeError('Введенное значение не является целым числом')
    if n<0:
        raise ValueError('Введенное значение явлется отрицательным числом')
    result=[]
    for i in range(n+1):
        result.append(line(i))
    return result
   
class Test_Check(TestCase):
    def test_Cel(self):
        self.assertEqual(Pascal_trianngle(0),[[1]])
        self.assertEqual(Pascal_trianngle(1),[[1],[1,1]])
        self.assertEqual(Pascal_trianngle(4),[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
    def test_string(self):
        self.assertRaises(TypeError, Pascal_trianngle, 'lol')
    def test_string1(self):
        self.assertRaises(TypeError, Pascal_trianngle, '')
    def test_string2(self):
        self.assertRaises(TypeError, Pascal_trianngle, ' ')
    def test_neg(self):
        self.assertRaises(ValueError, Pascal_trianngle, -6)
    def test_neg1(self):
        self.assertRaises(ValueError, Pascal_trianngle, -321)
        
main()
