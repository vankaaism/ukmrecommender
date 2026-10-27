from pythonapp.urutkanposisi import urutkan_jarak


def cari_mirip(data, rating_user, jumlah):
    daftar = []
    for mhs in data:
        total = 0
        for i in range(len(rating_user)):
            selisih = rating_user[i] - mhs.rating[i]
            total = total + selisih * selisih
        jarak = total ** 0.5
        daftar.append([jarak, mhs])

    daftar = urutkan_jarak(daftar)

    hasil = []
    for i in range(min(jumlah, len(daftar))):
        hasil.append(daftar[i][1])
    return hasil
