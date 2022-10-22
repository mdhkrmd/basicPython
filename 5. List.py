# List
nama = [1,2,3,4,5]
# nama = [1,2,3,[4,5]]
# print(nama[3][1])
# Tambah
c = 0
for x in nama:
    c += x
print(c)
nama.append("Muhammad")
nama.append("Andhika")
nama.append("Ramadhan")

print(nama)

#Itung jumlah data dalam list
print(len(nama))

#Panggil list
print(nama[0], nama[4])

print(" ")

#Hapus salah satu data dalam list
print("Setelah dihapus")
nama.remove("Ramadhan")
print(nama)
print(len(nama))
print(nama[1], nama[3])

#Belajar input data kedalam list
# a = input("Masukan nama :")
# nama.append(a)
# print(nama)

print(" ")

#Edit List
print("Setelah diubah")
nama[3] = "Fadhli"
print(nama)
print(nama[1] ,nama[3])

print("\n")

contoh_list = [1, 'dua', 3, 4.0, 5]
print(contoh_list)
print(contoh_list[0])

#tambah tengah (indeks ke, isi baru)
del(contoh_list[1])
contoh_list.insert(2,'Andhika')
print(contoh_list)
print(contoh_list[3])
#akses data paling belakang [-1]
print(contoh_list[-1])
contoh_list = [1, 'dua', 3, 4.0, 5]
contoh_list[3] = 'empat'
print(contoh_list[3])

print("\n")

a = [1,2,3,4,5,1,3,7,8,10,5,'a','b','c','d','e']
print(a.count(1)) #hitung banyaknya elemen yang sama
print(a.index(4)) #posisi index dari elemen pertama yang ditemukan
a.reverse() #sort balik
print(a)
#a.sort() sort kalo tipe data sama
print("\n")
#(1,101,2) artinya range 1 sampai 101-2 dengan lompatan 2 -> 1,3,5,7,....
b = list(range(1,101,2))
for x in b:
    print(x)
print("Total:",sum(b), "Nilai Max:", max(b), "Nilai Min:", min(b), '\n')

ax = [1,2,3,4,5]
bx = [5,4,3,2,1]
cx = []
dx = []
# fungsi zip -> menggabungkan nilai dari dua buah iterables (misal: list,tuple) ke dalam satu iterable

ex = list(range(1,101,2))
for fx in ex:
    dx.append((fx**2))
print(dx)
print("")

gx = 0
gx = [(gx**2) for gx in ex]
print(gx)
print("")

for (x) in zip(ax, bx):
    print(x)
print("")

for (a,b) in zip(ax, bx):
    cx.append((a+b)**2)
print(cx)