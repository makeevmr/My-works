from unittest import TestCase, main

def perfect_numb(a):
    if type(a)!=int:
        raise TypeError('Введенное значение не является целым числом')
    if a < 0 or a == 0:
        raise ValueError('Введенное значение не является положительным числом')
    sum=0
    for i in range (1,a//2+1):
        if a%i==0:
            sum=sum+i
    if a==sum:
        return True
    else:
        return False
class Test_Perfect_Numb(TestCase):
    def test_true(self):
        self.assertTrue(perfect_numb(6))
        self.assertTrue(perfect_numb(28))
        self.assertTrue(perfect_numb(496))
        self.assertTrue(perfect_numb(8128))
    def test_false(self):
        self.assertFalse(perfect_numb(2))
        self.assertFalse(perfect_numb(9))
        self.assertFalse(perfect_numb(7))
        self.assertFalse(perfect_numb(1))
    def test_error_string(self):
        self.assertRaises(TypeError, perfect_numb, 'lol')
        self.assertRaises(TypeError, perfect_numb, '')
        self.assertRaises(TypeError, perfect_numb, ' ')
    def test_error_neg(self):
        self.assertRaises(ValueError, perfect_numb, -8)
        self.assertRaises(ValueError, perfect_numb, -41)
main()
