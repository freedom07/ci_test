import unittest

from project_1 import add


class TestProject1(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    @unittest.skip
    def test_mul(self):
        self.fail()
