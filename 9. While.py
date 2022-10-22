#while (perulangan berkondisi), melakukan perulangan berdasarkan kondisi boolean
#perulangan akan terus terjadi ketika while bernilai true
#maka dari itu, untuk memberhentikan perulangan, harus diinput false

nama = ""

while nama != "andhika":
    nama = input("Masukan nama : ")
    if nama != "andhika":
        print("salah")

print("sip nama bener")

#========================================

bilangan = 1
while bilangan < 10:
    print(bilangan)
    bilangan += 1

a = 1
nilai = int(input("Masukan tinggi: "))
while a < nilai:
    b = 1
    while b < a:
        print("*", end='')
        b += 1
    print()
    a += 1

