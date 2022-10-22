# Definisikan class Karyawan berikut dengan attribut dan fungsinya
class Karyawan:
    nama_perusahaan = 'ABC'
    insentif_lembur = 250000
    def __init__(self, nama, umur, gaji, name2):
        self.nama = nama
        self.umur = umur
        self.gaji = gaji
        self.nama_perusahaan2 = name2
    def lembur(self):
        self.gaji += self.insentif_lembur
    def tambahan_proyek(self, tambah):
        self.gaji += tambah
    def total_pendapatan(self):
        return self.gaji 
# Buat object dari karyawan bernama Aksara dan Senja
aksara = Karyawan('Aksara', 25, 9500000, 'DEF')
senja = Karyawan('Senja', 28, 12500000, 'FED')

# Aksara melaksanakan lembur
aksara.lembur()

# Senja memiliki proyek tambahan
senja.tambahan_proyek(2500000)

# Cetak pendapatan total Aksara dan Senja
print('Pendapatan Total Aksara: ' + str(aksara.total_pendapatan()))
print('Pendapatan Total Senja: ' +str(senja.total_pendapatan()))
print(aksara.__class__.nama_perusahaan)
print(senja.__class__.nama_perusahaan)
print(aksara.nama_perusahaan2)
print(senja.nama_perusahaan2)