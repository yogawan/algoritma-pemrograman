import datetime as dt

# date and time

hari_ini = dt.date.today()
print(hari_ini)
print(f"hari ini hari = {hari_ini:%A}")

tanggal = dt.date(2005,1,29)
print(tanggal)
print(f"hari ini hari = {tanggal:%A}")