from math import factorial
from unittest import TestCase, main



def line(m):
    lst=[]
    for i in range(m+1):
        C=factorial(m)/(factorial(m-i)*factorial(i))
        C=int(C)
        lst.append(C)
    return lst


def Pascal_trianngle(n):
    l=0
    if type(n)!=str:
        if n>-1 and type(n)==int:
            l=1
            result=[]
            for i in range(n+1):
                result.append(line(i))
            return result
    try:
        e=1/l
    except ZeroDivisionError:
        print('Степень в треугольнике паскаля целое число большее или равное 0')
class test_check(TestCase):
    def test_Cel(self):
        self.assertEqual(Pascal_trianngle(0),[[1]])
        self.assertEqual(Pascal_trianngle(1),[[1],[1,1]])
        self.assertEqual(Pascal_trianngle(4),[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

main()
