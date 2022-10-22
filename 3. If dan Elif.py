# If
kpk = 1000
polri = 100

if kpk < polri:
    print("cicak kalah oleh buaya")

if kpk > polri:
    print("cicak menang lawan buaya")

if kpk == polri:
    print("cicak vs buaya")

print()

# else
menang = False

if menang == True:
    print("alhamdulillah")

else:
    print("bangkit lagi")

print()
# elif
nilai = int(input("Masukan nilai anda: "))

if nilai >= 90:
    print("Mantap")
elif nilai >= 80:
    print("Mayan")
elif nilai >= 70:
    print("Remed")
else:
    print("Belajar ulang\n")
    
angka = range(1,100)
for i in angka:
    if(i%2 == 0):
        print(i, "Genap")
    else:
        print(i, "Ganjil")
