from os import remove
from re import compile
import unittest
import amu


class amu_should(unittest.TestCase):

    def test_is_menu(self):
        name = 'menu'
        regex = compile(rf'(\[.*?\]\((..\/)*\) > |{name})')
        true = lambda x: self.assertTrue(amu.is_menu(x, regex))
        false = lambda x: self.assertFalse(amu.is_menu(x, regex))

        true('[menu](../) > page')
        true('[menu](../../) > [page1](../) > page2')
        false('[menu](http://foo.bar) > page')
        false('Some plain text')
        true('menu')

if __name__ == '__main__': unittest.main()
