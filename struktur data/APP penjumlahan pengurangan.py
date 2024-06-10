# Meminta pengguna untuk memilih operasi
print("Silakan pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
operasi = input("Masukkan nomor operasi yang ingin Anda lakukan (1/2): ")

# Memeriksa operasi yang dipilih
if operasi == '1':
    # Jika operasi yang dipilih adalah penjumlahan
    bilangan1 = int(input("Masukkan bilangan pertama: "))
    bilangan2 = int(input("Masukkan bilangan kedua: "))
    hasil = bilangan1 + bilangan2
    print("Hasil penjumlahan:", hasil)
elif operasi == '2':
    # Jika operasi yang dipilih adalah pengurangan
    bilangan1 = int(input("Masukkan bilangan pertama: "))
    bilangan2 = int(input("Masukkan bilangan kedua: "))
    hasil = bilangan1 - bilangan2
    print("Hasil pengurangan:", hasil)
else:
    print("Operasi yang dimasukkan tidak valid.")
