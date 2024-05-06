# latihan perulangan atau looping membuat segitiga

sisi = int(input("masukan angka untuk ukuran segitiga : "))

# mengunakan for
print("for")
count = 1
for i in range(sisi):
    print("x"*count)
    count += 1
print("selesai")

# mengunakan while
print("while")
count = 1
while True:
    print("x"*count)
    count += 1
    if count > sisi:
        break
print("selesai")

# hanya ganjil saja
print("mulai")
count = 1
while True:
    if (count%2):
        # print jika ganjil
        print("x"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break
print("selesai")

# print segitiga
count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        # print jika ganjil
        print(" "*spasi, "x"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break
print("selesai")

# 5. ketupat
print("ketupat")
print("   *   ")
print("  ***  ")
print(" ***** ")
print("*******")
print(" ***** ")
print("  ***  ")
print("   *   ")