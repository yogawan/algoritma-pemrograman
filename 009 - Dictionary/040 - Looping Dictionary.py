# looping dictionary

teman_teman = {
    "yog":"yoga adit",
    "tam":"tama yoga",
    "dit":"aditya pratama",
    "sof":"sofik andre",
    "ris":"riski wahyu"
}

# loop biasa
print("loop biasa")
for teman in teman_teman:
    print(teman)

# loop keys #1
print("mengunakan keys #1")
for key in teman_teman.keys():
    print(key)

# loop keys #2
print("mengunakan keys #2")
for key in teman_teman.keys():
    print(teman_teman.get(key))

# value
print("mengunakan value")
for value in teman_teman.values():
    print(value)

# items
print("mengunakan items")
for items in teman_teman.items():
    print(items)

# mengabungkan keys dengan value
print("mengabungkan keys dengan value")
for keys, value in teman_teman.items():
    print(f"keys : {keys}, value : {value}") 