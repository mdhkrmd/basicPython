contoh_list = ['Dewi', 'Budi', 'Cici', 'Linda', 'Cici'] 
print(contoh_list)
contoh_set = {'Dewi', 'Budi', 'Cici', 'Linda', 'Cici'}
print(contoh_set)
contoh_set.add('Andhika')
print(contoh_set)
contoh_frozen_set = ({'Dewi', 'Budi', 'Cici', 'Linda', 'Cici'})
print(contoh_frozen_set)
contoh_frozen_set.add('Andhika')
print(contoh_frozen_set)

# Berbeda dengan tipe data set, tipe data list memperdulikan urutan dari setiap elemen saat list dideklarasikan.
# Berbeda dengan list yang mengizinkan adanya duplikasi elemen, 
# tipe data set tidak mengizinkan adanya elemen dengan nilai yang sama di dalamnya.

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.

# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.