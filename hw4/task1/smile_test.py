from unittest import TestCase, main
from smile_logic import smile_logic


class Test_smile(TestCase):
    def test_true(self):
        self.assertTrue(smile_logic(''))
        self.assertTrue(smile_logic('sidhvaaaiw *&348679!$!536'))
        self.assertTrue(smile_logic('((){}[()]443vw{23})'))
        self.assertTrue(smile_logic('[]{}()'))
        self.assertTrue(smile_logic('[]'))

    def test_false(self):
        self.assertFalse(smile_logic('[{]}'))
        self.assertFalse(smile_logic('пРифФкИи [) >3'))
        self.assertFalse(smile_logic('(**245))231'))
        self.assertFalse(smile_logic('{'))
        self.assertFalse(smile_logic(']]'))


main()
