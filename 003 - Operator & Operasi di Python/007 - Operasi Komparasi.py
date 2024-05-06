# operasi komparasi

# setiap hasil dari komparasi-komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# 1. lebih besar dari >
print("_______ lebih besar dari (>) _______")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# 2. kurang dari <
print("_______ kurang dari (<) _______")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# 3. lebih dari sama dengan >=
print("_______ lebih dari sama dengan (>=) _______")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# 4. kurang dari sama dengan <=
print("_______ kurang dari sama dengan (<=) _______")
hasil = a >= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# 5. sama dengan ==
print("_______ sama dengan (==) _______")
hasil = a == 3
print(a,'==',3,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)
hasil = b == 2
print(b,'==',2,'=',hasil)

# 6. tidak sama dengan !=
print("_______ tidak sama dengan (!=) _______")
hasil = a != 3
print(a,'!=',3,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)
hasil = b != 2
print(b,'!=',2,'=',hasil)

# 7. is / is not sebagai komparasi objek identitas
print("_______ objek identitas (!=) _______")
x = 5 # ini adalaha assigment membuat objek
y = 5

print('nilai x = ,',x,', id =',hex(id(x)))
print('nilai y = ,',y,', id =',hex(id(y)))

hasil = x is 5
print('x is 5 =',hasil)