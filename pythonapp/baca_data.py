# class Mahasiswa:
#     def __init__(self, nama, prodi, angkatan, rating, ukm):
#         self.nama = nama
#         self.prodi = prodi
#         self.angkatan = angkatan
#         self.rating = rating
#         self.ukm = ukm


def baca_data(nama_file):
    daftar = []

    file = open(nama_file, "r")
    baris_baris = file.readlines()
    file.close()

    # Membaca data mulai dari baris kedua
    for baris in baris_baris[1:]:
        baris = baris.strip()

        if baris == "":
            continue

        kolom = baris.split(",")

        nama = kolom[0]
        prodi = kolom[1]
        angkatan = int(kolom[2])

        # Mengambil 12 rating mahasiswa
        jumlah_dimensi = 12  
        rating = []

        for i in range(3, 3 + jumlah_dimensi):
            rating.append(int(kolom[i]))

         # Mengambil UKM dari kolom terakhir
        ukm = kolom[3 + jumlah_dimensi]

        # Membuat dan menyimpan objek mahasiswa
        daftar.append(Mahasiswa(nama, prodi, angkatan, rating, ukm))
    
    return daftar

# Menguji hasil fungsi baca_data
# data = baca_data("kode/data/anggota.csv")

# print("=== HASIL PENGUJIAN BACA DATA ===")

# print("Jumlah mahasiswa:", len(data))
# print("Jumlah rating:", len(data[0].rating))
# print("Tipe rating:", type(data[0].rating[0]))
# print("Tipe angkatan:", type(data[0].angkatan))

# # Memeriksa apakah semua syarat terpenuhi
# assert len(data) == 40
# assert len(data[0].rating) == 12
# assert isinstance(data[0].rating[0], int)
# assert isinstance(data[0].angkatan, int)

# print("Semua pengujian berhasil!")
