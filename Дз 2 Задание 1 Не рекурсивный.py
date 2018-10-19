import unittest
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
    
  # Используемые значения при подсчете времени затрачиваемого на программу:
#300
#450
#600
#750
#900
#При всех вышеуказзаных значениях программа вычисления факториала, записанная без использования рекурсии, работает быстрее. 
#Связано это с тем, что при рекурсивном варианте работы программа "пробегает" функцию большое количесвто раз, когда как не рекурсивная программа все время работает внутри одной функции.
#Поэтому в рекурсивном варианте работы совершается намного больше действий, что влечет за собой потерю скорости работы программы. 
    
    
    
    
    
    
    
    
    
    
    

