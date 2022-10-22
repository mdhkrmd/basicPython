#local
file = open("hello.txt", "r")
baca = file.read()
#baca2 = file.readlines() # dalam bentuk list
# baca_baris1 = file.readline() # baca perbaris
# baca_baris2 = file.readline()
# for teks in file:
#     print(teks) # metode loop
file.close()
print(baca, "\n")
#   print(baca2, "\n")
# print(baca_baris1)
# print(baca_baris2)

# r: read, hanya untuk membaca saja
# w: write, mode ini dapat aku gunakan untuk menulis ke dalam sebuah berkas teks. Jika berkas tidak tersedia, maka Python akan secara otomatis membuat sebuah berkas baru dengan nama yang telah di spesifikasikan. Saat menulis dengan menggunakan mode ini, jika file semula tidak kosong, maka isi yang sebelumnya terdapat di dalam berkas akan terhapus.
# a: append, mode ini dapat aku gunakan untuk menambahkan isi dari sebuah berkas teks. Mode ini juga akan membuat sebuah berkas teks baru dengan nama yang telah kita spesifikasikan jika berkas teks tidak tersedia.
# w+: write+, mode ini dapat aku gunakan untuk membaca ataupun menuliskan isi dari sebuah berkas teks.
# a+: append+, mode ini dapat aku gunakan untuk membaca ataupun menambahkan isi dari sebuah berkas teks

# Menulis ke file hello.txt
file = open("hello.txt", "w")
file.write("Sekarang kita belajar menulis dengan menggunakan Python")
file.write("Menulis konten file dengan mode w (write).")
file.close()

# Menulis ke file dengan mode append
file = open("hello.txt", "a")
file.writelines([
"Sekarang kita belajar menulis dengan menggunakan Python", 
" Menulis konten file dengan mode a (append)."
])
file.close()

#url
from urllib import response
import requests
url = "https://storage.googleapis.com/dqlab-dataset/hello.txt"
response = requests.get(url)
print(response, "\n") # response 200 artinya berhasil terbaca
# for baris in response.iter_lines():
#     print(baris) # metode loop
print(response.text)