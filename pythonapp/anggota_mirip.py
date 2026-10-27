def tampilkan_anggota(anggota):
    print("\n" + "=" * 45)
    print("ANGGOTA DENGAN MINAT YANG PALING MIRIP")
    print("=" * 45)
    for i in range(len(anggota)):
        mhs = anggota[i]
        if mhs.izin == "ya":
            print(str(i + 1) + ". " + mhs.nama + " (" + mhs.prodi + ") - " + mhs.ukm)
        else:
            print(str(i + 1) + ". Annonym - " + mhs.ukm)
