x,y,z = 1,2,3
print(x,y,z)

x,y = y,z
print(x,y)

c = 0
for i in range (1,6):
    c = c + i
print(c)

print("a"*5)
print("an" in "andhika")
a = 4
print(bin(a))

b = "b"
B = "B"
d = ord(b) > ord(B)
print(ord(b), ord(B))
print(d)

huruf = ['a','b','c','d','e']
for v in huruf:
    print(v,"\n")

import math
print(math.sqrt(100))

angka = range(1,101)
angka2 = [1,2,3,4,5]
print(len(angka))
print(len(angka2))

inp = input("Masukan apa saja: ")
print(inp)

ang1 = int(input("masukan angka awal = "))
ang2 = int(input("masukan angka kedua = "))
op = ang1 + ang2
print(op)