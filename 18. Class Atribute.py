# Definisikan class Karyawan
# class merupakan kerangka untuk objek
class Karyawan:
    nama_perusahaan = 'ABC' # -> merupakan class atribute, jika diubah maka akan mempengaruhi seluruh objek
    # class atribute bernilai sama untuk seluruh objek
    # instance atribute bernilai berbeda untuk setiap objek
    
# Inisiasi object yang dinyatakan dalam variabel aksara dan senja
# disini aksara dan senja merupakan objek
aksara = Karyawan()
senja = Karyawan()

# Cetak nama perusahaan melalui penggunaan keyword __class__
# pada class attribute nama_perusahaan
print(aksara.__class__.nama_perusahaan)

# Ubah nama_perusahaan menjadi 'DEF'
# dikarenakan nama_perusahaan merupakan class atribute maka apabila ingin mengganti, cukup melalui satu objek saja
# maka senja akan terpengaruhi
aksara.__class__.nama_perusahaan = 'AND'

# Cetak nama_perusahaan objek aksara dan senja
print(aksara.__class__.nama_perusahaan)
print(senja.__class__.nama_perusahaan)