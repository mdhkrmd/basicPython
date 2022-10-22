nama    = []
umur    = []
alamat  = []

jumlah = int(input("Masukan Jumlah data orang yang diinginkan : "))
print("==========================================================")

for a in range (0, jumlah):
    input_nama = input(f"Masukan nama orang ke {a} : ")
    input_umur = int(input(f"Masukan umur orang ke {a} : "))
    input_alamat = input(f"Masukan alamat orang ke {a} : ")
    nama.append(input_nama)
    umur.append(input_umur)
    alamat.append(input_alamat)
    print("====================")
    
for i in range (0, len(umur)): #len(umur) jangan jadi patokan, pake nama atau alamat juga bisa, pasti seragam jumlah datanya
    print(f"nama orang ke {i} : {nama[i]}")
    print(f"umur orang ke {i} : {umur[i]}")
    print(f"alamat orang ke {i} : {alamat[i]}")