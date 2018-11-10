from unittest import TestCase, main
from poly_logic import poly_logic


class Test_poly(TestCase):

    def test_equal(self):
        self.assertEqual(poly_logic('0'), '')
        string = '21x^6+50x^4-8x'
        self.assertEqual(poly_logic('3x^7 + 10x^5 - 4x^2 + 3'), string)
        self.assertEqual(poly_logic('0x^3+7x^0-2x+4'), '-2')
        self.assertEqual(poly_logic('1x^0-4x^1'), '-4')
        self.assertEqual(poly_logic('x^2+0x-4x^0-x^5'), '2x-5x^4')
        self.assertEqual(poly_logic('0'), '')


main()
