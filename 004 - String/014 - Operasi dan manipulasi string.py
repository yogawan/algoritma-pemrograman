# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case
salam = "bro"
salam = salam.upper()
print("upper : " + salam)

# merubah semua ke lower case
lowcase = "BRO"
lowcase = lowcase.lower()
print("lower = " + lowcase)

## pengecekan dengan isX method

# contoh pengecekan uppercase
data = "hallo para ahli kubur "
apakah_lower = data.islower()
print(data + "is lower : " + str(apakah_lower))

# contoh pengecekan uppercase
data = "HALLO PARA AHLI KUBUR "
apakah_upper = data.isupper()
print(data + "is upper : " + str(apakah_upper))

# isalpha() untuk mengecek semua huruf
# isalnum() untuk mengecek huruf dan angka
# isdecimal() untuk mengecek angka saja
# isspace() untuk mengecek spasi, tab, newline, \n
# istitle() semua kata dimulai dengan huruf besar


# istitle()
judul = "Semua Orang Sedang Bernafas"
cek_judul = judul.istitle()
print(judul + " is title : " + str(cek_judul))

## ngecek komponen
cek_start = "Moba Analok".startswith("Moba")
print("start = " + str(cek_start))

cek_end = "Moba Analok".startswith("Analok")
print("end = " + str(cek_end))

## pengabungan komponen join() split()
pisah = ['aku','sayang','kamu']
# koma
gabung = ', '.join(pisah)
print(gabung)
# spasi
gabung = ' '.join(pisah)
print(gabung)
# string
gabung = ' hehe '.join(pisah)
print(gabung)
# split
gabong = "akugaksayanggakkamu"
print(gabong.split('gak'))

# alokasi karakter rjust(), ljust(), center()

# rjust()
kanan = " kanan ".rjust(10,"=")
print("'" + kanan + "'")

# ljust()
kiri = " kiri ".ljust(10,"=")
print("'" + kiri + "'")

# center()
tengah = " tengah ".center(20,"=")
print("" + tengah + "")