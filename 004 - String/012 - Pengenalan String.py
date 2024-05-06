data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

# 1.1 mengunakan single qoute '...'
data = 'mengunakan single qoute'
print(data)
# 1.2 mengunakan doble qoute "..."
data_kedua = "mengunakan doble qoute"
print(data_kedua)
# 1.3 doble qoute atau single qoute di dalam string
print('"halo, apa kabar semuanya"')
print("'halo, apa kabar semuanya'")
print("hari ini adalah hari senin, eehh selasa ding")

# 2. mengunakan tanda \

# 2.1 membuat tanda ' menjadi string
print("mari sholat jum\'at")
# 2.2 backlash
print("c:\\user\\yogawan")
# 2.3 tab
print("yogawan\tasw, pepeg kau")
# 2.4 backspace
print("yogawan\basw")
# 2.5 newline
print("baris pertama\nbaris kedua\nbaris ketiga")

# 3. string literal atau raw

# 3.1 hati hati
print('c:\new folder') # salah
# 3.2 mengunakan raw string
print(r'c:\new folder') # benar
# 3.3 multiline literal string
print("""
nama : yogawan
npm : 5220411056
prodi : informatika
kampus : universitas teknologi yogyakarta
""")
# 3.4 multiline literal string dan raw
print(r"""
nama : yogawan
npm : 5220411056
prodi : informatika
kampus : universitas teknologi yogyakarta
web : www.tesla.com/yogawan
""")