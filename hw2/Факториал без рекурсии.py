import unittest
from memory_profiler import profile
@profile
def factorial(a):
    k=1
    if type(a)!=int:
        raise TypeError('Введенное значение не является целым числом')
    if a < 0:
        raise ValueError('Введенное значение явлется отрицательным числом')
    if a==0:
        return 1
    for i in range(1,a+1):
        k=k*i
    return k
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
    
  # Используемые значения при подсчете времени затрачиваемого на программу:
#300
#Время: Нерекурсивный 0,0002356470000000055
        #Рекурсивный  0,0004815000000000236
#5
#Память: Нерекурсивный 17,7 MiB
          #Рекурсивный 17,9 MiB
  
#450
#Время: Нерекурсивный 0,000194521000000000305
        #Рекурсивный  0,001099888700000000216
#15
#Память: Нерекусивный 17,7 MiB
          #Рекурсивный 17,7 MiB

#600
#Время: Нерекурсивный 0,00033230800000000034
        #Рекурсивный  0,001618911999999999724
#25
#Память: Нерекурсивный 17,7 MiB
          #Рекурсивный 17,9 MiB
#750
#Время: Нерекурсивный 0,0003437150000000222
       #Рекурсивный  0,0021502429999999996
#50
#Память: Нерекурсиный 17,7 MiB
         #Рекурсивный 18,2 MiB
  
#900
#Время: Нерекурсивный 0,0011001869999999747
        #Рекурсвный   0,001510544000000000026
#75
#Память: Нерекурсивный 17,7 MiB
          #Рекурсивный 18,3 MiB
#Вывод:
#Рекурсионный способ занимает больше памяти и дольше выполняется, чем нерекурсионный.
#Каждая рекурсия добавляет в стек памяти новый уровень, что увеличивает время исполнения и затраты памяти.
