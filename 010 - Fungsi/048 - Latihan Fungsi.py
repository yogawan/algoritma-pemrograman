# header
# os.system("clear")
# print(f"{'program menghitung luas':^40}")
# print(f"{'dan keliling persegi panjang':^40}")
# print(f"{'- '*20:^40}")

# mengambil input user
# lebar = int(input("masukan nilai lebar : "))
# panjang = int(input("masukan nilai panjang : "))

# menghitung luas
# luas = lebar*panjang
# keliling = 2*(lebar + panjang)

# hasil
# print(f"luas persegi adalah {luas}")
# print(f"luas keliling adalah {keliling}")

import os

def header():
    os.system("clear")
    print(f"{'program menghitung luas':^40}")
    print(f"{'dan keliling persegi panjang':^40}")
    print(f"{'- '*20:^40}")

def input_user():
    lebar = int(input("masukan nilai lebar : "))
    panjang = int(input("masukan nilai panjang : "))
    return lebar,panjang

def hitung():
    luas = lebar*panjang
    keliling = 2*(lebar + panjang)
    return luas,keliling

def hasil():
    print(f"luas persegi adalah : {luas}")
    print(f"luas keliling adalah : {keliling}")
    return

while True:
    header()
    lebar,panjang = input_user()
    luas,keliling = hitung()
    hasil()
    isContinue = input("apakah lanjut (y/n)? ")
    if isContinue == "n":
        break
print("program selesai")