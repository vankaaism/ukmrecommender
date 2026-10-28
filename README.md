# Temu: Rekomendasi UKM Cakrawala

Temu adalah program berbasis CLI (Command Line Interface) yang membantu mahasiswa baru memilih UKM yang sesuai dengan minat dan motivasinya.

## Latar Belakang

Selain prestasi akademik, relasi sosial ikut menentukan arah karier seseorang. Seibert, Kraimer, dan Liden (2001) menemukan bahwa modal sosial, yaitu jaringan relasi yang dimiliki seseorang, berhubungan dengan akses yang lebih baik ke informasi, sumber daya, dan dukungan karier, yang pada akhirnya berkaitan dengan kesuksesan karier.

Bagi mahasiswa, UKM adalah salah satu tempat paling alami untuk mulai membangun modal sosial. Masalahnya, mahasiswa baru sering bingung memilih UKM karena belum mengenal pilihannya, sehingga memilih secara acak atau sekadar ikut teman. Temu membantu dengan membandingkan minat dan motivasi pengguna dengan anggota UKM yang sudah ada.

## Dasar Penyusunan Pertanyaan

Pertanyaan di `Call_question.py` diadaptasi dari dua kerangka teori psikologi.

**Bagian A: Preferensi kegiatan (pertanyaan 1–6)** diadaptasi dari enam tipe minat dalam teori Holland (RIASEC), sebagaimana ditinjau oleh Nauta (2010):

| No | Tipe | Pernyataan menyangkut |
|---|---|---|
| 1 | Realistic | kegiatan fisik atau memakai tangan |
| 2 | Investigative | menyelidiki dan menganalisis |
| 3 | Artistic | berekspresi lewat karya |
| 4 | Social | membantu dan mengajar orang lain |
| 5 | Enterprising | memimpin dan meyakinkan orang |
| 6 | Conventional | pekerjaan rapi dan terstruktur |

**Bagian B: Motivasi ikut organisasi (pertanyaan 7–12)** diadaptasi dari enam fungsi motivasi dalam Volunteer Functions Inventory (Clary dkk., 1998):

| No | Fungsi | Pernyataan menyangkut |
|---|---|---|
| 7 | Values | memperjuangkan hal yang dianggap penting |
| 8 | Understanding | mempelajari keterampilan baru |
| 9 | Social | dekat dengan teman dan merasa menjadi bagian kelompok |
| 10 | Career | pengalaman dan relasi untuk karier |
| 11 | Protective | melepas penat dari tekanan |
| 12 | Enhancement | menjadi lebih percaya diri dan berkembang |

Pernyataan-pernyataan ini adalah adaptasi sederhana untuk keperluan program, bukan alat ukur psikologi yang sudah divalidasi.

## Cara Kerja

1. Program membaca data anggota UKM dari data/anggota.csv.
2. Pengguna menjawab 12 pernyataan dengan skala 1 sampai 5.
3. Program menghitung jarak Euclidean antara jawaban pengguna dan jawaban setiap anggota. Makin kecil jaraknya, makin mirip minatnya.
4. Lima anggota dengan jarak terkecil dipilih.
5. UKM kelima anggota itu dihitung sebagai suara, lalu diubah menjadi persentase.
6. Program menampilkan rekomendasi UKM, diurutkan dari persentase tertinggi.
7. Program menampilkan kelima anggota tersebut sebagai teman yang minatnya mirip.

## Privasi

Setiap anggota punya kolom izin di data. Nama dan prodi anggota hanya ditampilkan jika ia menjawab ya. Jika menjawab tidak, ia tetap ikut dihitung dalam rekomendasi, tetapi ditampilkan tanpa identitas, hanya UKM-nya.

Seluruh data di repo ini adalah data dummy, bukan data mahasiswa sungguhan.

## Menjalankan Program

Panduan ini ditulis untuk yang belum pernah menjalankan program Python sama sekali.

### Langkah 1: Pasang Python

1. Buka https://www.python.org/downloads/
2. Klik tombol *Download Python* (versi 3 apa pun bisa).
3. Jalankan file yang terunduh.
   - *Windows:* di jendela pertama, *centang "Add python.exe to PATH"* sebelum klik *Install Now*. Langkah ini penting. Tanpa itu, perintah python tidak akan dikenali.
   - *macOS:* ikuti petunjuk pemasangan sampai selesai.

Cek apakah Python sudah terpasang dengan membuka terminal:

- *Windows:* tekan tombol Windows, ketik cmd, tekan Enter.
- *macOS:* tekan Cmd + Spasi, ketik Terminal, tekan Enter.

Lalu ketik:


python --version


Di macOS, gunakan python3 --version. Kalau muncul tulisan seperti Python 3.12.0, Python sudah siap.

### Langkah 2: Unduh program

1. Buka halaman repo ini di GitHub.
2. Klik tombol hijau *Code, lalu pilih **Download ZIP*.
3. Ekstrak file ZIP yang terunduh (klik kanan, lalu *Extract All* di Windows, atau klik dua kali di macOS).
4. Akan muncul folder bernama ukmrecommender-main.

### Langkah 3: Buka terminal di folder program

*Windows:* buka folder ukmrecommender-main di File Explorer, klik kolom alamat di bagian atas, ketik cmd, lalu tekan Enter. Terminal langsung terbuka di folder itu.

*macOS:* di Terminal, ketik cd ` (dengan spasi setelahnya), seret folder `ukmrecommender-main ke jendela Terminal, lalu tekan Enter.

Pastikan kamu berada di folder yang benar dengan mengetik dir (Windows) atau ls (macOS). Harus terlihat main.py, data, pythonapp, dan tests.

### Langkah 4: Jalankan program


python main.py


Di macOS, gunakan python3 main.py. Program akan menampilkan pertanyaan pertama. Lanjutkan ke *Panduan Pengguna* di bawah.

### Menjalankan unit test (opsional)

Dari folder yang sama:


python -m unittest discover tests


Kalau semua berhasil, di baris terakhir muncul OK.

### Jika terjadi masalah

| Pesan yang muncul | Penyebab | Solusi |
|---|---|---|
| 'python' is not recognized... | Python belum terpasang atau "Add to PATH" tidak dicentang | Pasang ulang Python dan centang "Add python.exe to PATH", atau coba perintah py main.py |
| command not found: python (macOS) | Di macOS perintahnya python3 | Gunakan python3 main.py |
| FileNotFoundError: ... data/anggota.csv | Terminal tidak dibuka di folder program | Ulangi Langkah 3 sampai main.py terlihat saat mengetik dir atau ls |
| can't open file 'main.py' | Terminal tidak dibuka di folder program | Ulangi Langkah 3 |

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
| 4 atau ` 4 ` (dengan spasi) | Diterima |
| kosong (langsung Enter) | Ditolak |
| abc | Ditolak, bukan angka |
| 0, 6 | Ditolak, di luar rentang |
| -1, 3.5 | Ditolak, bukan bilangan bulat 1 sampai 5 |

Setelah 12 pernyataan dijawab, program menampilkan rekomendasi UKM beserta persentasenya, lalu lima anggota dengan minat paling mirip.

