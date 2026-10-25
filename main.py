from pythonapp.data import baca_data
from pythonapp.input_user import minta_rating
from pythonapp.kemiripan import cari_mirip
from pythonapp.voting import hitung_suara


def main():
    data = baca_data("data/ukm.csv")              # 1. baca CSV
    rating_user = minta_rating()                  # 2. tanya preferensi user
    mirip = cari_mirip(data, rating_user, 5)      # 3. cari mahasiswa paling mirip
    hasil = hitung_suara(mirip)                   # 4. suara UKM -> persen -> urut
    # 5. tampilkan rekomendasi UKM dan nama anggota yang mirip


if __name__ == "__main__":
    main()
