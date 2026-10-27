def urutkan_jarak(daftar):
    n = len(daftar)
    for i in range(n):
        for j in range(n - 1 - i):
            if daftar[j][0] > daftar[j + 1][0]:
                sementara = daftar[j]
                daftar[j] = daftar[j + 1]
                daftar[j + 1] = sementara
    return daftar
