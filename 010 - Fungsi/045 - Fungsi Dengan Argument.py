# fungsi dengan argument input

# def nama_fungsi(argument):
#     badan fungsi

# contoh

# string
def oligarki(nama):
    print(f"selamat datang {nama} si kapitalis")

nama = input("masukan nama : ")
oligarki(nama)

# penjumplahan integer
def penjumplahan(angka_0,angka_1):
    hasil = angka_0 + angka_1
    print(f"hasil dari {angka_0} + {angka_1} adalah : {hasil}")

angka_0 = int(input("masukan angka : "))
angka_1 = int(input("masukan angka : "))
penjumplahan(angka_0,angka_1)

# def list
def daf_pe(list):
    data_peserta = list.copy()
    for peserta in data_peserta:
        print(f"yang terhormat : {peserta}")

list = ["yoga","miko","sandy","atha"]
daf_pe(list)