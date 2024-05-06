# width dan multiline

# data

data_nama = "yogawan adit"
data_umur = 18
data_tinggi = 170.1
data_ukuran_sepatu = 44

# string standar

data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, ukuran sepatu = {data_ukuran_sepatu}"
print(10*"="+" data string "+10*"=")
print(data_string)

# string multiline (\n)

data_string = f"nama = {data_nama} \numur = {data_umur} \ntinggi = {data_tinggi} \nukuran sepatu = {data_ukuran_sepatu}"
print(10*"="+" data string "+10*"=")
print(data_string)

# string multiline (tiga tanda kutip)

print(10*"="+" data string "+10*"=")
data_string = f"""
nama    = {data_nama}
umur    = {data_umur}
tinggi  = {data_tinggi}
sepatu  = {data_ukuran_sepatu}
"""

print(data_string)