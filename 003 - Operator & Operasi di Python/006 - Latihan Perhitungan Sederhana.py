# konversi celcius ke satuan lain
print("program konversi temperature celcius ke satuan lain")

celcius = float(input("masukan suhu dalam celcius : "))
print("suhu adalah",celcius,"celcius")

# celcius ke reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur,"reamur")

# celcius ke fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahrenheit,"fahrenheit")

# celcius ke kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah",kelvin,"kelvin")