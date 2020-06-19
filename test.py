import unittest

from project_1 import add
from project_1 import mul


class TestProject1(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_mul(self):
        self.assertEqual(mul(1, 2), 2)

    def test_div(self):
        self.assertEqual(mul(2, 1), 2)
