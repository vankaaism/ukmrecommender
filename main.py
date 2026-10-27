from pythonapp.baca_data import baca_data
from pythonapp.Call_question import minta_rating
from pythonapp.eucledian import cari_mirip
from pythonapp.hitung_suara import hitung_suara
from pythonapp.hasil import tampilkan_hasil


def main():
    print("=" * 45)
    print("TEMU - Rekomendasi UKM Cakrawala")
    print("=" * 45)

    data = baca_data("data/anggota.csv")
    rating_user = minta_rating()
    anggota = cari_mirip(data, rating_user, 5)
    suara = hitung_suara(anggota)
    tampilkan_hasil(suara)


if __name__ == "__main__":
    main()
