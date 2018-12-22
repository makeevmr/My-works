from unittest import TestCase, main
from Bulls_and_cows_logic import get_bull_count, get_cow_count


class Test_get_count(TestCase):

    def test_1(self):
        chl = '137825'
        secret_numb = '567126'
        self.assertEqual(get_bull_count(chl, secret_numb), 2)
        chl = '531425'
        secret_numb = '567126'
        self.assertEqual(get_bull_count(chl, secret_numb), 2)
        chl = '1'
        secret_numb = '1'
        self.assertEqual(get_bull_count(chl, secret_numb), 1)

    def test_2(self):
        chl = '137825'
        secret_numb = '561726'
        self.assertEqual(get_cow_count(chl, secret_numb), 4)
        chl = '531427'
        secret_numb = '657126'
        self.assertEqual(get_cow_count(chl, secret_numb), 4)
        chl = '10'
        secret_numb = '01'
        self.assertEqual(get_cow_count(chl, secret_numb), 2)


main()
