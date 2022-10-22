print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilih = input("Masukan pilihan: ")

if pilih == "1":
    print("Ini Pertambahan")
    a = int(input("Masukan angka pertama: "))
    b = int(input("Masukan angka kedua: "))
    hasil = a + b
    print("Maka", a ," + ", b, " = ", hasil)

elif pilih == "2":
    print("Ini Pengurangan")
    a = int(input("Masukan angka pertama: "))
    b = int(input("Masukan angka kedua: "))
    hasil = a - b
    print(f"Maka: {a} - {b} = {hasil}")

elif pilih == "3":
    print("Ini Perkalian")
    a = int(input("Masukan angka pertama: "))
    b = int(input("Masukan angka kedua: "))
    hasil = a * b
    print(f"Maka: {a} * {b} = {hasil}")

elif pilih == "4":
    print("Ini Pembagian")
    a = int(input("Masukan angka pertama: "))
    b = int(input("Masukan angka kedua: "))
    hasil = a / b
    print(f"Maka: {a} / {b} = {hasil}")

else:
    print("Maaf, pilihan tak ada")