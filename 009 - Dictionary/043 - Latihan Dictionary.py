import datetime
import os

# template mahasiswa
mahasiswa_template = {
	'nama':'nama',
	'nim':'0000000000',
	'sks_lulus':0,
	'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    # os.system("cls") # windows
    os.system("clear") # macos

    # header
    print(f"{'selamat datang di data mahasiswa':^40}")
    print(f"{'universitas teknologi yogyakarta':^40}")
    print("-"*40)

    # mahasiswa
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    # nama mahasiswa
    mahasiswa['nama'] = input("nama mahasiswa : ")

    # nim mahasiswa
    mahasiswa['nim'] = input("nim mahasiswa : ")

    # sks mahasiswa
    mahasiswa['sks_lulus'] = int(input("sks mahasiswa : "))

    # tanggal lahir mahasiswa
    # input
    tahun_lahir = int(input("tahun lahir : "))
    bulan_lahir = int(input("bulan lahir : "))
    tanggal_lahir = int(input("tanggal lahir : "))
    # select
    mahasiswa['lahir']:datetime.datetime(tahun_lahir,bulan_lahir,tanggal_lahir)
    print(mahasiswa)