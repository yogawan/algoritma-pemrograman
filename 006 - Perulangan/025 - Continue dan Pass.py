# continue, pass, break

# pass, berfungsi sebagai dummy
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        print("whatsapp man")
    elif angka == 5:
        print("whatsapp bro")
    print(angka)

# continue
angka = 0
print(f"angka sekarang {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang {angka}")
    print("whatsapp")
print("nice")