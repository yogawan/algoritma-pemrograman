# operasi logika atau boolean
# not, or, and, xor

# not
print("_____ not _____")
a = False
c = not a
print('data a =',a)
print("_____ not _____")
print('data c =',c)

# or (jika salah satu true, maka hasilnya adalah ture)
print("_____ or _____")
a = False
b = False
c = a or b
print(a, 'or' ,b, '=' ,c)
a = False
b = True
c = a or b
print(a, 'or' ,b, '=' ,c)
a = True
b = False
c = a or b
print(a, 'or' ,b, '=' ,c)
a = True
b = True
c = a or b
print(a, 'or' ,b, '=' ,c)

# and (jika dua buah nilai true, maka hasil true)
print("_____ and _____")
a = False
b = False
c = a and b
print(a, 'and' ,b, '=' ,c)
a = False
b = True
c = a and b
print(a, 'and' ,b, '=' ,c)
a = True
b = False
c = a and b
print(a, 'and' ,b, '=' ,c)
a = True
b = True
c = a and b
print(a, 'and' ,b, '=' ,c)

# xor (jika dua buah nilai true, maka hasil true)
print("_____ xor _____")
a = False
b = False
c = a ^ b
print(a, 'xor' ,b, '=' ,c)
a = False
b = True
c = a ^ b
print(a, 'xor' ,b, '=' ,c)
a = True
b = False
c = a ^ b
print(a, 'xor' ,b, '=' ,c)
a = True
b = True
c = a ^ b
print(a, 'xor' ,b, '=' ,c)