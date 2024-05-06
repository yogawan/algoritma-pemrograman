# while input

data_int = int(input("hitung sampai : "))

angka = 0
while True:
    angka += 1
    print(f"count : {angka}")
    if angka == data_int:
        break
print("selesai")