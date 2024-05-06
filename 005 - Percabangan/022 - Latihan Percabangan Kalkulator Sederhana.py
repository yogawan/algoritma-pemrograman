# kalkulator sederhana
program = "kalkulator sederhana"
print(program)

angka_pertama = float(input("masukan angka : "))
operator = input("operator (+,-,x,/) : ")
angka_kedua = float(input("masukan angka : "))

# percabangan
if operator == "+":
    hasil = angka_pertama + angka_kedua
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_pertama - angka_kedua
    print(f"hasilnya adalah {hasil}")
elif operator == "x":
    hasil = angka_pertama * angka_kedua
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_pertama / angka_kedua
    print(f"hasilnya adalah {hasil}")
else:
    print("tidak bisa menjumplahkan angka karena tidak ada operator operasi, operator yang tersedia (+,-,x,/)")