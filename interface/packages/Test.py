import unittest

from interface.packages.Element import Element
from interface.packages.IO import IO


class TestElement(unittest.TestCase):
    PORT: str = '/dev/ttyACM0'

    def test_create_element_length(self):
        i: Element = Element("cuve",
                             [IO('d:13:o', 'resistance'), IO('d:12:o', 'cap_temp_1'), IO('d:11:o', 'cap_temp_2')],
                             True,self.PORT)
        self.assertEqual(len(i.ios().values()), 3)

    def test_regex_element(self):
        with self.assertRaises(ValueError):
            Element("cuve", [IO('g:13:o', 'resistance')],
                    self.PORT)

        with self.assertRaises(ValueError):
            Element("cuve", [IO('g:13:o', 'resistance')],
                    self.PORT)

        with self.assertRaises(ValueError):
            Element("cuve", [IO(':13:u', 'resistance')],
                    self.PORT)

        with self.assertRaises(ValueError):
            Element("cuve", [IO('gd:13a:o', 'resistance')],
                    self.PORT)


if __name__ == '__main__':
    unittest.main()
