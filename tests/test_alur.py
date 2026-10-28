import unittest

from pythonapp.baca_data import baca_data
from pythonapp.hitung_suara import hitung_suara
from pythonapp.eucledian import cari_mirip


class TestAlur(unittest.TestCase):
    def test_data_terbaca(self):
        data = baca_data("data/anggota.csv")
        self.assertEqual(len(data), 40)
        self.assertEqual(len(data[0].rating), 12)

    def test_kolom_izin_terbaca(self):
        data = baca_data("data/anggota.csv")
        for mhs in data:
            self.assertTrue(mhs.izin == "ya" or mhs.izin == "tidak")

    def test_suara_dari_mahasiswa_mirip(self):
        data = baca_data("data/anggota.csv")
        anggota = cari_mirip(data, [5, 5, 2, 2, 3, 3, 2, 5, 3, 4, 2, 3], 5)
        suara = hitung_suara(anggota)
        self.assertEqual(suara[0][0], "Robotic")


if __name__ == "__main__":
    unittest.main()
