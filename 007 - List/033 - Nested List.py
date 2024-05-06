# nested list

# list biasa
print("nested list")
list_biasa = [1,2,3,4,5,6,7,8]
print(f"data list biasa {list_biasa}")

# list 2 dimensi
data_0 = [1,2,3,4,]
data_1 = [5,6,7,8,]

list_2_dimensi = [data_0,data_1,list_biasa]
print(f"list dua dimensi : {list_2_dimensi} \n")

# contoh pengunaan
peserta_0 = ["ucup",25,"laki-laki"]
peserta_1 = ["asep",20,"laki-laki"]
peserta_2 = ["tama",18,"laki-laki"]
peserta_3 = ["miko",18,"laki-laki"]
peserta_4 = ["atha",18,"laki-laki"]
peserta_5 = ["tina",18,"perempuan"]

list_peserta = [peserta_0,peserta_1,peserta_2,peserta_3,peserta_4,peserta_5]

print(f"list peserta : {list_peserta} \n")

for peserta in list_peserta:
    print(f"nama : {peserta[0]}")
    print(f"umur : {peserta[1]}")
    print(f"jenis kelamin : {peserta[2]} \n")