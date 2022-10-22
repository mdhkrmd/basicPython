class Karyawan:
    nama_perusahaan = 'ABC'
    def __init__(self, nama, umur, gaji):
        self.nama = nama
        self.umur = umur
        self.gaji = gaji
        # instance attribute ditandai dengan def __init__ (self, parameter1, ..., parameterN)

# Buat object bernama aksara dan senja
aksara = Karyawan('Aksara', 25, 8500000)
senja = Karyawan('Senja', 28, 12500000)

# aksara.__class__.nama -> class attribute
# aksara.nama -> instance attribute

print(aksara.nama, aksara.umur, aksara.gaji, aksara.__class__.nama_perusahaan)
print(senja.nama, senja.umur, senja.gaji, senja.__class__.nama_perusahaan)