# default argument

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya):

# contoh 1
def say_hello(nama = "ganteng \n"):
    print(f"hallo {nama}")

say_hello("tama")
say_hello()

# contoh 2
def sapa_dia(nama,pesan = "apa kabar \n"):
    print(f"hai {nama}, {pesan}")
sapa_dia("tama","banyak bacot kamu yah") 
sapa_dia("tama")

# contoh 3
def hitung_pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil

angka_0 = int(input("masukan angka : "))
angka_1 = int(input("masukan pangkat : "))
print(hitung_pangkat(angka_0,angka_1))

# contoh 4
def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil
print(fungsi())
print(fungsi(input3=10))