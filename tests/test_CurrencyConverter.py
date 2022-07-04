import unittest
from modules.CurrencyConverter import CurrencyConverter


class TestCurrencyConverter(unittest.TestCase):
    def test_get_val_by_ident(self):
        cc = CurrencyConverter()
        self.assertTrue(cc.currencies.__getitem__, 'USD')
        self.assertRaises(KeyError, cc.currencies.__getitem__, 'RUR')


    def test_convert(self):
        cc = CurrencyConverter()
        self.assertEqual(cc.convert(1000, 'RUR', 'RUR'), 1000.0)
        self.assertEqual(cc.convert(1, 'USD', 'RUR'), round(cc.get_val_by_ident('USD'), 2))
