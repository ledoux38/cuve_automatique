import unittest

from interface.packages.Element import Element
from interface.packages.GPIO import GPIO


class TestElement(unittest.TestCase):
    def test_create_element_length(self):
        i: Element = Element("cuve", [GPIO('d:13:o'), GPIO('d:12:o'), GPIO('d:11:o')])
        self.assertEqual(len(i.get_gpio_all()), 3)

    def test_create_element(self):
        i: Element = Element("cuve", [GPIO('d:13:o'), GPIO('d:12:o'), GPIO('d:11:o')])
        self.assertEqual(i.get_gpio_index(0).get_name(), 'd:13:o')
        self.assertEqual(i.get_gpio_index(0).get_address(), 13)

    def test_regex_element(self):
        with self.assertRaises(ValueError):
            Element("cuve", [GPIO('g:13:o')])


if __name__ == '__main__':
    unittest.main()
