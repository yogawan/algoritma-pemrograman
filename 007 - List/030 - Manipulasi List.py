# operasi list

# index     0(-3)    1(-2)    2(-1)
data = ["yogawan","aditya","pratama"]

# cara mengambil data
data_0 = data[0]
print(f"data 0 adalah : {data_0}")

data_1 = data[1]
print(f"data 1 adalah : {data_1}")

data_2 = data[2]
print(f"data 2 adalah : {data_2}")

# cara mengambil data terakhir
data_terakhir = data[-1]
print(f"data terakhir adalah : {data_terakhir}")

# mengambil info data dari list
panjang_data = len(data)
print(f"panjang data adalah : {panjang_data}")

# manipulasi data list
print(f"data sebelum di tambah : \n{data}")

data.insert(1,"asadel")
print(f"data setelah di tambah : \n{data}")

# akhir list
data.append("tamael")
print(f"data setelah di tambah : \n{data}")

# cara menambah data baru
data_baru = ["spartan","soldier","yogaadit"]
data.extend(data_baru)
print(data)

# merubah data
data[2] = "maikel"
print(data)

# menghapus data

# data.remove("maikel","yogaadit")
# print(data)
# akan eror karena used

data_akhir = data.pop()
print(data)