# latihan logika dan komparasi

# membuat gabungan area rentan dari angka

# +++++++3-------10++++++++

# inputUser = float(input("masukan angka yang bernilai \nkurang dari 3\natau \nlebih besar dari 10 : "))

# +++++++3-------
# # memeriksa angka kurang dari 3
# isiKurangDari = (inputUser < 3)

# # -------10++++++++
# # memeriksa angka lebih dari 10
# isiLebihDari = (inputUser > 10)

# # +++++++3-------10++++++++
# isCorrect = isiKurangDari or isiLebihDari
# print("angka yang anda masukan = ",isCorrect)

# -------3+++++++10-------
inputUser = float(input("masukan angka yang bernilai \nlebih besar dari 3\ndan \nkurang dari 10 : "))
isiLebihDari = (inputUser > 3)
isiKurangDari = (inputUser < 10)

isCorrect = isiLebihDari and isiKurangDari
print("angka yang anda masukan = ",isCorrect)