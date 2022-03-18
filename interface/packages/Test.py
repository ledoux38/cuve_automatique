import unittest

from interface.packages.Element import Element
from interface.packages.GPIO import GPIO


class TestElement(unittest.TestCase):
    def test_create_element_length(self):
        i: Element = Element("cuve",
                             [GPIO('d:13:o', 'resistance'), GPIO('d:12:o', 'cap_temp_1'), GPIO('d:11:o', 'cap_temp_2')])
        self.assertEqual(len(i.gpios), 3)

    def test_create_element(self):
        i: Element = Element("cuve",
                             [GPIO('d:13:o', 'resistance'), GPIO('d:12:o', 'cap_temp_1'), GPIO('d:11:o', 'cap_temp_2')])
        self.assertEqual(i.get_gpio_index(0).get_name(), 'd:13:o')
        self.assertEqual(i.get_gpio_index(0).address, 13)

    def test_regex_element(self):
        with self.assertRaises(ValueError):
            Element("cuve", [GPIO('g:13:o', 'resistance')])

        with self.assertRaises(ValueError):
            Element("cuve", [GPIO('g:13:o', 'resistance')])

        with self.assertRaises(ValueError):
            Element("cuve", [GPIO(':13:u', 'resistance')])

        with self.assertRaises(ValueError):
            Element("cuve", [GPIO('gd:13a:o', 'resistance')])

    def test_get_gpio(self):
        i: Element = Element("cuve",
                             [GPIO('d:13:o', 'resistance'), GPIO('d:12:o', 'cap_temp_1'), GPIO('d:11:o', 'cap_temp_2')])
        self.assertEqual(i.get_gpio_index(0).get_name(), 'd:13:o')
        self.assertEqual(i.get_gpio_index(0).address, 13)

    def test_search_gpio(self):
        i: Element = Element("cuve",
                             [GPIO('d:13:o', 'resistance'), GPIO('d:12:o', 'cap_temp_1'), GPIO('d:11:o', 'cap_temp_2')])
        self.assertEqual(i.search_gpio('cap_temp_1').get_name(), 'd:12:o')


if __name__ == '__main__':
    unittest.main()
