# teknik menduplikat list
print("data a dan b")

a = ["kamu","bacot","sekali","kawan","delogok","kamu","yah"]
print(f"a : {a}")

b = a
print(f"b : {b} \n")

# merubah number dari a
print("data a dan b setelah index di replace")

a[0] = "kau"

print(f"a : {a}")
print(f"b : {b} \n")

# short data
print("data setelah di short")

b.sort()
print(f"b : {b} \n")

# addres dari kedua list a dan list b
print("addres a dan addres b")

print(f"addres a : {hex(id(a))}")
print(f"addres b : {hex(id(b))} \n")

# menduplikat list dengan copy
print("menduplikat list dengan copy")

c = a.copy()
print(f"c : {c}")

print(f"addres a : {hex(id(a))}")
print(f"addres b : {hex(id(b))}")
print(f"addres c : {hex(id(c))} \n")

print("data sekarang")
print(f"a : {a}")
print(f"b : {b}")
print(f"c : {c} \n")

# ubah salah satu data
c[0] = "astaga"

print("ubah salah satu data")
print(f"a : {a}")
print(f"b : {b}")
print(f"c : {c}")