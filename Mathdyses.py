import numpy as np

def hitung_aljabar_linier():
    print("\n=== Menghitung Aljabar Linier ===")
    
    A = np.array(eval(input("Masukkan koefisien matriks A: ")))
    B = np.array(eval(input("Masukkan koefisien vektor B: ")))

    try:
        solusi = np.linalg.solve(A, B)
        print("Hasil Solusi Persamaan Linier:")
        print(solusi)
    except np.linalg.LinAlgError:
        print("Sistem persamaan linier tidak memiliki solusi unik.")

def kalkulator_matriks():
    print("\n=== Kalkulator Matriks ===")
    
    matriks_a = np.array(eval(input("Masukkan matriks A: ")))
    matriks_b = np.array(eval(input("Masukkan matriks B: ")))

    print("\nPilih operasi matriks:")
    print("1. Penjumlahan Matriks")
    print("2. Pengurangan Matriks")
    print("3. Perkalian Matriks")
    print("4. Kembali ke Menu Utama")

    choice = int(input("Pilih operasi (1/2/3/4): "))

    if choice == 1:
        hasil = matriks_a + matriks_b
        print("\nHasil Penjumlahan Matriks:")
        print(hasil)
    elif choice == 2:
        hasil = matriks_a - matriks_b
        print("\nHasil Pengurangan Matriks:")
        print(hasil)
    elif choice == 3:
        hasil = np.dot(matriks_a, matriks_b)
        print("\nHasil Perkalian Matriks:")
        print(hasil)
    elif choice == 4:
        return
    else:
        print("Pilihan tidak valid. Kembali ke Menu Utama.")

def kalkulator_vektor():
    print("\n=== Kalkulator Vektor ===")
    
    vektor_a = np.array(eval(input("Masukkan vektor A: ")))
    vektor_b = np.array(eval(input("Masukkan vektor B: ")))

    print("\nPilih operasi vektor:")
    print("1. Penjumlahan Vektor")
    print("2. Pengurangan Vektor")
    print("3. Perkalian Skalar dengan Vektor")
    print("4. Kembali ke Menu Utama")

    choice = int(input("Pilih operasi (1/2/3/4): "))

    if choice == 1:
        hasil = vektor_a + vektor_b
        print("\nHasil Penjumlahan Vektor:")
        print(hasil)
    elif choice == 2:
        hasil = vektor_a - vektor_b
        print("\nHasil Pengurangan Vektor:")
        print(hasil)
    elif choice == 3:
        skalar = float(input("Masukkan nilai skalar: "))
        hasil = skalar * vektor_a
        print("\nHasil Perkalian Skalar dengan Vektor:")
        print(hasil)
    elif choice == 4:
        return
    else:
        print("Pilihan tidak valid. Kembali ke Menu Utama.")

def hitung_matriks_inverse():
    print("\n=== Menghitung Matriks Inverse ===")
    
    matriks = np.array(eval(input("Masukkan matriks: ")))

    try:
        hasil = np.linalg.inv(matriks)
        print("\nHasil Matriks Inverse:")
        print(hasil)
    except np.linalg.LinAlgError:
        print("Matriks tidak memiliki invers.")

def hitung_matriks_determinan():
    print("\n=== Menghitung Matriks Determinan ===")
    
    matriks = np.array(eval(input("Masukkan matriks: ")))

    hasil = np.linalg.det(matriks)
    print(f"\nHasil Matriks Determinan: {hasil}")

def menu_program():
    while True:
        print("\nMenu Kalkulator:")
        print("1. Menghitung Aljabar Linier")
        print("2. Kalkulator Matriks")
        print("3. Kalkulator Vektor")
        print("4. Menghitung Matriks Inverse")
        print("5. Menghitung Matriks Determinan")
        print("6. Keluar")

        choice = int(input("Pilih menu (1/2/3/4/5/6): "))
        
        if choice == 1:
            hitung_aljabar_linier()
        elif choice == 2:
            kalkulator_matriks()
        elif choice == 3:
            kalkulator_vektor()
        elif choice == 4:
            hitung_matriks_inverse()
        elif choice == 5:
            hitung_matriks_determinan()
        elif choice == 6:
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")


menu_program()
