# Temu: Rekomendasi UKM Cakrawala

Temu adalah program berbasis CLI (Command Line Interface) yang membantu mahasiswa baru memilih UKM yang sesuai dengan minat dan motivasinya.

## Latar Belakang

Selain prestasi akademik, keterlibatan sosial ikut memengaruhi perkembangan dan arah karier mahasiswa. Lewat UKM, mahasiswa membangun relasi dan modal sosial. Masalahnya, mahasiswa baru sering bingung memilih UKM karena belum mengenal pilihannya. Temu menjawab masalah itu dengan membandingkan jawaban pengguna dengan jawaban anggota UKM yang sudah ada.

## Cara Kerja

1. Program membaca data anggota UKM dari `data/anggota.csv`.
2. Pengguna menjawab 12 pernyataan dengan skala 1 sampai 5:
   - Bagian A: preferensi kegiatan
   - Bagian B: motivasi ikut organisasi
3. Program menghitung jarak Euclidean antara jawaban pengguna dan jawaban setiap anggota. Makin kecil jaraknya, makin mirip minatnya.
4. Lima anggota dengan jarak terkecil dipilih.
5. UKM kelima anggota itu dihitung sebagai suara, lalu diubah menjadi persentase.
6. Program menampilkan rekomendasi UKM, diurutkan dari persentase tertinggi.
7. Program menampilkan kelima anggota tersebut sebagai teman yang minatnya mirip.

## Privasi

Setiap anggota punya kolom `izin` di data. Nama dan prodi anggota hanya ditampilkan jika ia menjawab `ya`. Jika menjawab `tidak`, ia tetap ikut dihitung dalam rekomendasi, tetapi ditampilkan tanpa identitas, hanya UKM-nya.

Seluruh data di repo ini adalah data dummy, bukan data mahasiswa sungguhan.

## Menjalankan Program

Butuh Python 3, tanpa library tambahan. Jalankan dari folder utama repo:

```
python main.py
```

Menjalankan unit test:

```
python -m unittest discover tests
```

## Panduan Pengguna

Program menampilkan 12 pernyataan satu per satu. Untuk setiap pernyataan, ketik angka 1 sampai 5 lalu tekan Enter:

| Angka | Arti |
|---|---|
| 1 | Sangat tidak sesuai |
| 2 | Tidak sesuai |
| 3 | Netral |
| 4 | Sesuai |
| 5 | Sangat sesuai |

Input selain angka 1 sampai 5 akan ditolak, lalu pernyataan yang sama ditanyakan ulang:

| Contoh input | Hasil |
|---|---|
| `4` atau ` 4 ` (dengan spasi) | Diterima |
| kosong (langsung Enter) | Ditolak |
| `abc` | Ditolak, bukan angka |
| `0`, `6` | Ditolak, di luar rentang |
| `-1`, `3.5` | Ditolak, bukan bilangan bulat 1 sampai 5 |

Setelah 12 pernyataan dijawab, program menampilkan rekomendasi UKM beserta persentasenya, lalu lima anggota dengan minat paling mirip.

## Contoh Keluaran

```
=============================================
REKOMENDASI UKM UNTUKMU
=============================================
Nama UKM                   Suara   Persen
---------------------------------------------
English Club               3       60.00%
Cakrawala Business Club    1       20.00%
Arunika Motion             1       20.00%

Paling cocok: English Club

=============================================
ANGGOTA DENGAN MINAT YANG PALING MIRIP
=============================================
1. Rizky (Akuntansi) - English Club
2. Fajar (Manajemen) - English Club
3. Dimas (Hukum) - English Club
4. Annonym - Cakrawala Business Club
5. Delvino (Bisnis Digital) - Arunika Motion
```

## Struktur Folder

```
main.py                     alur utama program
data/
  anggota.csv               data dummy 40 anggota UKM
pythonapp/
  mahasiswa.py              class Mahasiswa
  baca_data.py              baca_data
  Call_question.py          nilai_valid, minta_rating
  eucledian.py              cari_mirip
  urutkanposisi.py          urutkan_jarak
  hitung_suara.py           hitung_suara
  hasil.py                  tampilkan_hasil
  anggota_mirip.py          tampilkan_anggota
tests/
  test_urutkanposisi.py
  test_eucledian.py
  test_alur.py
```

## Format Data

```
nama,prodi,angkatan,r1,r2,...,r12,ukm,izin
```

- `r1` sampai `r12` adalah jawaban 1-5 untuk 12 pernyataan di `Call_question.py`, dengan urutan yang sama.
- `ukm` adalah UKM yang diikuti anggota tersebut.
- `izin` berisi `ya` atau `tidak`, yaitu persetujuan anggota agar nama dan prodinya ditampilkan.

UKM yang tersedia: English Club, Robotic, Kelas Studi Pasar Modal, Cakrawala Business Club, Aksara, Cakraphonic, Arunika Motion, dan Basket.

## Penerapan Konsep Pemrograman

| Konsep | Penerapan |
|---|---|
| Variabel dan tipe data | `int`, `float`, `str`, dan `list` untuk menyimpan rating, jarak, dan nama UKM; konversi teks CSV ke `int` di `baca_data.py` dan angka ke teks dengan `str()` di `anggota_mirip.py` |
| Input dan output | `input()` di `Call_question.py`, `print()` di `hasil.py` dan `anggota_mirip.py` |
| Operator aritmatika | `-`, `*`, `**` untuk jarak di `eucledian.py`; `/` dan `*` untuk persentase di `hitung_suara.py` |
| Operator relasional | `>=` dan `<=` di `nilai_valid`, `>` dan `<` di pengurutan, `==` untuk mengecek izin |
| Operator logika | `and` dan `not` di `nilai_valid` |
| Percabangan | validasi jawaban, pengecekan baris kosong CSV, penghitungan suara, dan penentuan tampil atau tidaknya nama anggota |
| Perulangan | `for` untuk membaca data dan menghitung jarak, `while` untuk mengulang input yang tidak valid |
| Fungsi | setiap fungsi punya tugas yang jelas dan disimpan di file sendiri di `pythonapp/` |
| List | daftar rating, daftar anggota, dan daftar hasil suara |
| Manipulasi string | `strip()`, `split()`, `isdigit()`, penggabungan teks dengan `+`, dan format f-string untuk tabel |
| Class | `Mahasiswa` untuk menyimpan data setiap anggota |
| Unit test | folder `tests/`, menggunakan modul `unittest` |
