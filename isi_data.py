#soal 1
def perkalian(a, b) :
    hasil = 0
    for _ in range(a):
        hasil += b

#soal 2
def deret_bilangan_ganjil(bawah, atas):
    jump = 1
    if (bawah > atas):
        jump = -1
    for i in range(bawah, atas, jump):
        if (i % 2 == 1):
            print(i, end=" ")
    print()

#soal 3
def ips():
    n = int(input("Masukkan jumlah mata kuliah: "))
    sks = 3 * n
    sum_nilai = 0
    kamus = {
        "A": 4, "B": 3, "C": 2, "D": 1
	}
    for i in range(n):
        sum_nilai += kamus[(input(f"Nilai MK {i+1}? "))]
    print(f"Nilai IPS Anda semester ini {round(sum_nilai*3/sks, 2)}")
        
