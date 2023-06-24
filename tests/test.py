import unittest
from even_dist import fibo_sphere, plot_fibo_sphere


class test_fibo(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_zero(self):
        self.assertEqual(fibo_sphere(0), ([], [], []))
