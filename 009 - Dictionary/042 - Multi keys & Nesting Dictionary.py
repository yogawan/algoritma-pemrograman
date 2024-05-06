import datetime

mahasiswa_satu = {
	'nama':'agustina',
	'nim':'5220411055',
	'sks_lulus':150,
	'beasiswa':True,
	'lahir':datetime.datetime(2004,4,10)
}

mahasiswa_dua = {
	'nama':'yogawan',
	'nim':'5220411056',
	'sks_lulus':140,
	'beasiswa':False,
	'lahir':datetime.datetime(2004,10,10)
}

mahasiswa_tiga = {
	'nama':'sabilatul',
	'nim':'5220411057',
	'sks_lulus':150,
	'beasiswa':True,
	'lahir':datetime.datetime(2004,2,29)
}

data_mahasiswa = {
	'00001':mahasiswa_satu,
	'00002':mahasiswa_dua,
	'00003':mahasiswa_tiga
}

print(f"{'key':<6} {'nama':<17} {'sks':<3} {'beasiswa':<9} {'lahir':<10}")
print("-"*47)

for mahasiswa in data_mahasiswa:
	key = mahasiswa

	nama = data_mahasiswa[key]['nama']
	nim = data_mahasiswa[key]['nim']
	sks = data_mahasiswa[key]['sks_lulus']
	beasiswa = data_mahasiswa[key]['beasiswa']
	lahir = data_mahasiswa[key]['lahir'].strftime("%x")

	print(f"{key:<6} {nama:<17} {sks:<3} {beasiswa:^9} {lahir:<10}")