# format string

# string
nama = "yoga"
format_str = f"hello {nama}, apakabar, dari siapa"

print(format_str)

# boolean
bool = False
format_str = f"boolean = {bool}"

print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"

print(format_str)

# angka bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka}"

print(format_str)

# bilangan ribuan
angka = 2000
format_str = f"bilangan ribuan = {angka:,}"

print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"angka = {angka:.2f}"

print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"angka = {angka:010.3f}"

print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
angka_minus = f"angka minus = {angka_minus:+d}"
angka_plus = f"angka plus = {angka_plus:+d}"

print(angka_minus)
print(angka_plus)

# format persen
presentase = 0.045
format_persen = f"format persen = {presentase:.2%}"

print(format_persen)

# operasi dalam format string
harga = 100000
jumplah = 3

total_harga = f"total harga = {harga*jumplah:,}"
print(total_harga)

# format angka lain (binary, oktal, hex)
angka = 225
format_binary = f"binary = {bin(angka)}"
format_oktal = f"oktal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_oktal)
print(format_hex)