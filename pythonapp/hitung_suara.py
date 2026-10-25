def hitung_suara(tetangga):
    # Bagian 1: Menghitung suara setiap UKM
    nama_ukm = []
    jumlah = []

    for tetangga_i in tetangga:
        ukm = tetangga_i["ukm"]

        if ukm in nama_ukm:
            posisi = nama_ukm.index(ukm)
            jumlah[posisi] += 1
        else:
            nama_ukm.append(ukm)
            jumlah.append(1)

    # Bagian 2: Mengubah suara menjadi persen
    total = len(tetangga)
    hasil = []

    if total == 0:
        return hasil

    for i in range(len(nama_ukm)):
        persen = (jumlah[i] / total) * 100
        hasil.append([nama_ukm[i], jumlah[i], persen])

    # Bagian 3: Mengurutkan dari suara terbanyak
    n = len(hasil)

    for i in range(n):
        for j in range(n - 1 - i):
            if hasil[j][1] < hasil[j + 1][1]:
                sementara = hasil[j]
                hasil[j] = hasil[j + 1]
                hasil[j + 1] = sementara

    return hasil


# Contoh data tetangga
tetangga = [
    {"ukm": "English Club"},
    {"ukm": "Robotic"},
    {"ukm": "English Club"},
    {"ukm": "English Club"}, 
    {"ukm": "Aksara"},
    {"ukm": "Robotic"},
    {"ukm": "English Club"},
    {"ukm": "Aksara"}
]

# Menjalankan fungsi
hasil = hitung_suara(tetangga)

# Menampilkan hasil rekomendasi
print("HASIL REKOMENDASI UKM")
print("-" * 45)
print(f"{'Nama UKM':<20} {'Suara':<8} {'Persen'}")
print("-" * 45)

for ukm, suara, persen in hasil:
    print(f"{ukm:<20} {suara:<8} {persen:.2f}%")
