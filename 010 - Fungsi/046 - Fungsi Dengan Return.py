# fungsi dengan kembalian

# fungsi return
# def kuadrat(x):
#     hasil = x**2
#     return hasil

# input = int(input("masukan angka : "))
# a = kuadrat(input)
# print(f"hasil akar 2 : {a}")

# contoh return banyak operasi penjumplahan
def operasi_matematika(angka_0,angka_1):
    penjumplahan = angka_0 + angka_1
    pengurangan = angka_0 - angka_1
    pembagian = angka_0 / angka_1
    perkalian = angka_0 * angka_1
    return penjumplahan,pengurangan,pembagian,perkalian

angka_0 = int(input("masukan angka : "))
angka_1 = int(input("masukan angka : "))
w,x,y,z = operasi_matematika(angka_0,angka_1)

print(f"hasil penjumplahan = {w}")
print(f"hasil pengurangan= {x}")
print(f"hasil pembagian = {y}")
print(f"hasil perkalian = {z}")