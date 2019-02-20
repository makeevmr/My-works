from unittest import TestCase, main
from caesar_logic import encrypt, decrypt


class Test_caesar(TestCase):

    def test_equal_encrypt(self):
        self.assertEqual(encrypt(3, 'Hello world'), 'Khoor zruog')
        self.assertEqual(encrypt(25, 'ABc ASF 235 rqw'), 'ZAb ZRE 235 qpv')
        self.assertEqual(encrypt(-25, '[]@23@% SDVG'), '[]@23@% TEWH')
        self.assertEqual(encrypt(0, 'asd[}}00'), 'asd[}}00')
        self.assertEqual(encrypt(1, '$234*ABCDef'), '$234*BCDEfg')
        self.assertEqual(encrypt(12, ''), '')
        self.assertEqual(encrypt(-1, 'BCDE*767$#'), 'ABCD*767$#')

    def test_equal_decrypt(self):
        self.assertEqual(decrypt(3, 'Khoor zruog'), 'Hello world')
        self.assertEqual(decrypt(25, 'ZAb ZRE 235 qpv'), 'ABc ASF 235 rqw')
        self.assertEqual(decrypt(-25, '[]@23@% TEWH'), '[]@23@% SDVG')
        self.assertEqual(decrypt(0, 'asd[}}00'), 'asd[}}00')
        self.assertEqual(decrypt(1, '$234*BCDEfg'), '$234*ABCDef')
        self.assertEqual(decrypt(12, ''), '')
        self.assertEqual(decrypt(-1, 'ABCD*767$#'), 'BCDE*767$#')


main()
