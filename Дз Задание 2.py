from unittest import TestCase, main

def perfect_numb(a):
    if type(a)!=str:
        sum=0
        x=0
        if a>1 and type(a)==int:
            x=1
            for i in range (1,a//2+1):
                if a%i==0:
                    sum=sum+i
            if a==sum :
                return True
            else:
                return False
    try:
        p=1/x
    except:
        print('Введенное число не соотвтетствует условию совершенных чисел')
    
        
class test_perfect_numb(TestCase):
    def test_true(self):
        self.assertTrue(perfect_numb(6))
        self.assertTrue(perfect_numb(28))
        self.assertTrue(perfect_numb(496))
        self.assertTrue(perfect_numb(8128))
    def test_false(self):
        self.assertFalse(perfect_numb(2))
        self.assertFalse(perfect_numb(9))
        self.assertFalse(perfect_numb(7))
        
                
            
main()
