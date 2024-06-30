def main():
    # List untuk menyimpan angka-angka yang dimasukkan
    numbers = []
    
    while True:
        # Meminta pengguna memasukkan angka atau 'q' untuk keluar
        user_input = input("Masukkan angka (atau ketik 'q' untuk keluar): ")
        
        if user_input.lower() == 'q':
            # Jika pengguna mengetik 'q', keluar dari loop
            break
        
        try:
            # Mengonversi input menjadi float dan menambahkannya ke list
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            # Menangani input yang bukan angka
            print("Input tidak valid. Harap masukkan angka atau 'q' untuk keluar.")
    
    if numbers:
        # Menghitung rata-rata jika ada angka yang dimasukkan
        average = sum(numbers) / len(numbers)
        print(f"Rata-rata dari angka yang dimasukkan adalah: {average}")
    else:
        print("Tidak ada angka yang dimasukkan.")

# Memanggil fungsi main
if __name__ == "__main__":
    main()
