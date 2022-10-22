# digunakan untuk menskip proses perulangan 
# program yang berada di bawah statement tidak akan dieksekusi

angka = range(1, 101)

for i in angka:
    if i == 50:
        print(f"{i} Nilai ditemukan")
        continue
        print("GAAKAN DICETAK KARENA I SUDAH BERNILAI 50")
    print(i)