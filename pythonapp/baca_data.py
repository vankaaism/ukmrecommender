from pythonapp.mahasiswa import Mahasiswa


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


