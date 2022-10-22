def fungsi():
    a = 5
    b = 2
    print (a+b)

fungsi()

def luas_pp(panjang, lebar):
    luas = panjang * lebar
    return luas

print(luas_pp(5,6))

def cek(angka):
    hasil = angka % 2
    if(hasil == 0):
        return True
    else:
        return False

angka = int(input("Masukan angka :"))
print(cek(angka))