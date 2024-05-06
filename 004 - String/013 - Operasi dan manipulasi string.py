# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "yogawan"
nama_tengah = "aditya"
nama_akhir = "pratama"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " adalah = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

y = "y"
status = y in nama_lengkap
print(y + " ada di " + nama_lengkap + " = " + str(status))

Y = "Y"
status = Y in nama_lengkap
print(Y + " ada di " + nama_lengkap + " = " + str(status))

y = "y"
status = y not in nama_lengkap
print(y + "tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(0:8) : " + nama_lengkap[0:8])

# item paling kecil
print("item paling kecil : " + min(nama_lengkap))

# item paling besar
print("item paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah : " + str(ascii_code))
data = 177
print("char untuk ASCII code adalah : " + chr(data))

# 4. operator dalam bentuk method

data = "otong surotong tukang ngocong"
jumplah = data.count("o")

print("jumplah o pada data = " + str(jumplah))