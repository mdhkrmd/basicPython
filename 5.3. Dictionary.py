person = {
    'nama': 'John Doe', 
    'pekerjaan': 'Programmer'
}
print(person['nama'])
print(person['pekerjaan'])
print(len(person))
print(person.keys())
print(person.values())
print(person.items())
print("nama" in person)
print("John Doe" in person.values())
person['nama'] = 'Andhika'
person['pekerjaan'] = 'Machine Learning Engineer'
print(person['nama'])
print(person)

for x in person:
    print(x, ":", person[x])

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.

# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.