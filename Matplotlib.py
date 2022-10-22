import matplotlib.pyplot as plt

x = []
y = []

bates = int(input("Masukan jumlah koordinat yang diinginkan : "))

for a in range (0, bates):
    input_x = int(input(f"Masukan nilai x ke {a} : "))
    input_y = int(input(f"Masukan nilai y ke {a} : "))
    x.append(input_x)
    y.append(input_y)
    print("====================")

plt.plot(x, y, 'ro') # isi dari graph
plt.axis([0, 15, 0, 15]) # banyak jumlah nilai x dan y di graph (xmin, xmax, ymin, ymax)

plt.show()