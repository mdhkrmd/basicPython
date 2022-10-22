nilai = []
hasil = 0
tot = 0
a = 0

def hasil():
    print("Hasil rata-ratanya: ")
    
def hitung(nilai, banyak):
    for bx in nilai:
        global tot
        tot = tot + bx
        hasil = tot / banyak
    return hasil;

jumlah = int(input("Masukan jumlah data yang diinginkan: "))
for ax in range (0, jumlah):
    int_nilai = int(input(f"Masukan angka ke {ax}: "))
    nilai.append(int_nilai)
banyak  = len(nilai)
a = hitung(nilai, banyak)
hasil()
print(a)