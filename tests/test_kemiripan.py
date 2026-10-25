# Jalankan dari folder utama: python -m unittest discover tests
import unittest

from pythonapp.kemiripan import hitung_jarak


class TestKemiripan(unittest.TestCase):
    def test_rating_sama_jaraknya_nol(self):
        self.assertEqual(hitung_jarak([3, 4, 5], [3, 4, 5]), 0)


if __name__ == "__main__":
    unittest.main()
