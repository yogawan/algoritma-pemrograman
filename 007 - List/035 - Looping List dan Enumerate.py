# looping dari list

# list for loop

# list for loop integer
print("integer")
kumpulan_angka = [9,8,7,6,5,1,2,3,4]
for angka in kumpulan_angka:
    print(f"angka : {angka}")
print("\n")

# list for loop string
print("string")
peserta = ["yoga","tama","adit","tia","asa","del","ela"]
for nama in peserta:
    print(f"nama : {nama}")
print("\n")

# for loop in range
print("for loop range")
kumpulan_angka = [9,8,7,6,5,1,2,3,4]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"angka : {kumpulan_angka[i]}")
print("\n")

# while loop
print("while loop")
kumpulan_angka = [9,8,7,6,5,1,2,3,4]
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f"angka : {kumpulan_angka[i]}")
    i += 1
print("\n")