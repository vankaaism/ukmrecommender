# Temu: Rekomendasi UKM Cakrawala

Program CLI yang merekomendasikan UKM berdasarkan preferensi mahasiswa, beserta nama anggota yang minatnya mirip.

## Menjalankan

```
python main.py
```

Unit test:

```
python -m unittest discover tests
```

## Struktur

```
main.py                  titik masuk, hanya memanggil fungsi
data/ukm.csv             data dummy
pythonapp/
  data.py                baca_data
  input_user.py          nilai_valid, minta_rating
  voting.py              hitung_suara
  kemiripan.py           hitung_jarak, urutkan, cari_mirip
tests/                   unit test
```

## Kesepakatan format data

Semua fungsi memakai format mahasiswa yang sama:

```python
{"nama": "Budi", "prodi": "Informatika", "rating": [4, 2, 5], "ukm": "Aksara"}
```

- `baca_data` mengembalikan list berisi dictionary di atas.
- `minta_rating` mengembalikan list rating dengan urutan yang sama seperti kolom rating di CSV.
- `hitung_suara` mengembalikan list `(nama_ukm, persen)`, urut dari suara terbanyak.
