import unittest

from interface.packages.Element import Element
from interface.packages.GPIO import GPIO


class TestElement(unittest.TestCase):
    def test_create_element_length(self):
        i: Element = Element("cuve", [GPIO('d:13:o', 13), GPIO('d:12:o', 12), GPIO('d:11:o', 11)])
        self.assertEqual(len(i.get_gpio_all()), 3)

    def test_create_element(self):
        i: Element = Element("cuve", [GPIO('d:13:o', 13), GPIO('d:12:o', 12), GPIO('d:11:o', 11)])
        self.assertEqual(i.get_gpio_index(0).name, 'd:13:o')
        self.assertEqual(i.get_gpio_index(0).adress, 13)
        self.assertEqual(i.get_gpio_index(1).name, 'd:12:o')
        self.assertEqual(i.get_gpio_index(1).adress, 12)
        self.assertEqual(i.get_gpio_index(2).name, 'd:11:o')
        self.assertEqual(i.get_gpio_index(2).adress, 11)


if __name__ == '__main__':
    unittest.main()
