# count data
data_angka = [1,2,3,4,5,6,7,8,9]
print(data_angka)

count_data_1 = data_angka.count(1)
print(f"juplah data 1 adalah : {count_data_1}")

count_data_2 = data_angka.count(2)
print(f"juplah data 2 adalah : {count_data_2}")

count_data_3 = data_angka.count(3)
print(f"juplah data 3 adalah : {count_data_3}")

count_data_4 = data_angka.count(4)
print(f"juplah data 4 adalah : {count_data_4}")

count_data_5 = data_angka.count(5)
print(f"juplah data 5 adalah : {count_data_5}")

# ambil posisi data
data = ["yogawan","aditya","pratama"]

print(f"data = {data}")

index_satu = data.index("yogawan")
index_dua = data.index("aditya")
index_tiga = data.index("pratama")

print(f"index yogawan : {index_satu}")
print(f"index aditya : {index_dua}")
print(f"index pratama : {index_tiga}")

# mengurutkan list a-z


print(f"sebelum di short a-z : {data}")
data.sort() # huruf kecil ke besar
print(f"setelah di short a-z : {data}")

print(f"sebelum di short z-a : {data}")
data.reverse() # huruf besar ke kecil
print(f"setelah di short z-a : {data}")

# mengurutkan z-a

print(f"data angka 1-9 : {data_angka}")
data_angka.reverse() # angka besar ke kecil
print(f"data angka 9-1 : {data_angka}")

print(f"data angka 9-1 : {data_angka}")
data_angka.sort() # angka kecil ke besar
print(f"data angka 1-9 : {data_angka}")