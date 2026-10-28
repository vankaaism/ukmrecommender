import unittest

from pythonapp.urutkanposisi import urutkan_jarak


class TestUrutkanPosisi(unittest.TestCase):
    def test_urut_dari_terkecil(self):
        daftar = [[3.0, "C"], [1.0, "A"], [2.0, "B"]]
        hasil = urutkan_jarak(daftar)
        self.assertEqual([x[1] for x in hasil], ["A", "B", "C"])

    def test_daftar_kosong(self):
        self.assertEqual(urutkan_jarak([]), [])


if __name__ == "__main__":
    unittest.main()
