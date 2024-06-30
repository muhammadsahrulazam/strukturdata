def hitung_faktorial():
    while True:
        try:
            num = int(input("Masukkan angka untuk dihitung faktorialnya (angka negatif untuk berhenti): "))
            if num < 0:
                break
            faktorial = 1
            for i in range(1, num + 1):
                faktorial *= i
            print(f"Faktorial dari {num} adalah {faktorial}")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

hitung_faktorial()