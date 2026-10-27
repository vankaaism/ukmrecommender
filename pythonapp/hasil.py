def tampilkan_hasil(suara):
    print("\n" + "=" * 45)
    print("REKOMENDASI UKM UNTUKMU")
    print("=" * 45)
    print(f"{'Nama UKM':<26} {'Suara':<7} {'Persen'}")
    print("-" * 45)

    for ukm, jumlah, persen in suara:
        print(f"{ukm:<26} {jumlah:<7} {persen:.2f}%")

    if len(suara) > 0:
        print("\nPaling cocok: " + suara[0][0])

#  Testing dulu mas 
# suara = [
#     ["English Club", 3, 60.0],
#     ["Robotic", 1, 20.0],
#     ["Aksara", 1, 20.0]
# ]

# celuk fungsine
# tampilkan_hasil(suara)
