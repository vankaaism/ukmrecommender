NILAI_MIN = 1
NILAI_MAKS = 5

PERTANYAAN = [
    # Pertanyaan 1
    "Aku senang kegiatan yang memakai fisik atau tangan, seperti merakit, bergerak, atau mengoperasikan alat.",
    "Aku senang memecahkan masalah dengan menyelidiki, menganalisis, dan mencari tahu cara kerja sesuatu.",
    "Aku senang mengekspresikan diri lewat karya, seperti musik, tulisan, desain, atau pertunjukan.",
    "Aku senang kegiatan yang melibatkan membantu, mengajar, atau mendampingi orang lain.",
    "Aku senang memimpin, meyakinkan orang, atau menggerakkan sebuah tim menuju target.",
    "Aku senang pekerjaan yang rapi dan terstruktur, seperti mengelola data, angka, atau jadwal.",
    # Pertanyaan 2
    "Aku ingin ikut organisasi untuk memperjuangkan hal yang menurutku penting.",
    "Aku ingin ikut organisasi supaya bisa mempelajari keterampilan atau pengetahuan baru.",
    "Aku ingin ikut organisasi supaya bisa dekat dengan teman-teman dan merasa menjadi bagian dari kelompok.",
    "Aku ingin ikut organisasi supaya punya pengalaman dan relasi yang berguna untuk karierku.",
    "Aku ingin ikut organisasi supaya bisa melepas penat dari tekanan kuliah atau masalah pribadi.",
    "Aku ingin ikut organisasi supaya merasa lebih percaya diri dan berkembang sebagai pribadi.",
]

# FUNGSI 1: nilai_valid
def nilai_valid(teks):
    teks = teks.strip()
    if not teks.isdigit():
        return False
    angka = int(teks)
    return angka >= NILAI_MIN and angka <= NILAI_MAKS


# FUNGSI 2: minta_rating
def minta_rating():
    rating = []
    print("\nSeberapa sesuai pernyataan berikut dengan dirimu?")
    print("1 = sangat tidak sesuai, 2 = tidak sesuai, 3 = netral, 4 = sesuai, 5 = sangat sesuai")
    for i in range(len(PERTANYAAN)):
        if i == 0:
            print("\n-- Bagian A: Preferensi --")
        if i == 6:
            print("\n-- Bagian B: Motivasi ikut organisasi --")
        teks = str(i + 1) + ". " + PERTANYAAN[i] + "\n   Jawaban (1-5): "
        jawaban = input(teks)
        while not nilai_valid(jawaban):
            print("   Masukkan angka 1 sampai 5.")
            jawaban = input(teks)
        rating.append(int(jawaban))
    return rating


if __name__ == "__main__":
    hasil = minta_rating()
    print("\nRating kamu:", hasil)
    print("Jumlah jawaban:", len(hasil))