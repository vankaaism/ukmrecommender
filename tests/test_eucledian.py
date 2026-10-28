import unittest

from pythonapp.mahasiswa import Mahasiswa
from pythonapp.eucledian import cari_mirip


class TestEucledian(unittest.TestCase):
    def setUp(self):
        self.data = [
            Mahasiswa("Andi", "Informatika", 2025, [5, 5, 5], "Robotic", "ya"),
            Mahasiswa("Sari", "Sastra", 2025, [1, 1, 1], "Aksara", "ya"),
            Mahasiswa("Doni", "Manajemen", 2024, [4, 5, 4], "Robotic", "ya"),
        ]

    def test_rating_sama_paling_atas(self):
        hasil = cari_mirip(self.data, [1, 1, 1], 1)
        self.assertEqual(hasil[0].nama, "Sari")

    def test_urutan_dari_paling_mirip(self):
        hasil = cari_mirip(self.data, [5, 5, 5], 3)
        nama = []
        for mhs in hasil:
            nama.append(mhs.nama)
        self.assertEqual(nama, ["Andi", "Doni", "Sari"])

    def test_jumlah_lebih_dari_data(self):
        hasil = cari_mirip(self.data, [3, 3, 3], 10)
        self.assertEqual(len(hasil), 3)


if __name__ == "__main__":
    unittest.main()
