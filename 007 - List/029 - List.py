# list

# kumpulan data numbers
data_angka = [1,2,3,4,5]
print(data_angka)

# kumpulan data string
data_string = ["yogawan","aditya","pratama"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, False]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1,"yogawan",2,"aditya",3,"pratama"]
print(data_campuran)

# alternatif membuat list
data_range = range(0,10) # range start, stop, step
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop atau list comprehension
pangkat = int(input("masukan pangkat : "))
print(f"pangkat yang anda masukan adalah : {pangkat}")
list_pake_for = [i**(pangkat) for i in range(0,100)]
print(list_pake_for)

# membuat list pake for if
for_if = [i for i in range(0,10) if i != 5]
print(for_if)

genap = [i for i in range(0,10) if i%2 == 0]
print(genap)

ganjil = [i for i in range(0,10) if i%2 != 0]
print(ganjil)