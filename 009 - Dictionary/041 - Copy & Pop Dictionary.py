# copy dictionary

teman_teman = {
    "yog":"yoga adit",
    "tam":"tama yoga",
    "dit":"aditya pratama",
    "sof":"sofik andre",
    "ris":"riski wahyu"
}

teman = teman_teman.copy()

# copy
print(f"teman_teman : {teman_teman}")
print(f"teman : {teman} \n")

# update
teman_teman["yog"] = "yoga ganteng" 
print(f"teman_teman : {teman_teman}")
print(f"teman : {teman} \n")

# pop dictionary
data_yoga = teman.pop("yog")
print(f"data yoga : {data_yoga}")

print(f"data teman : {teman} \n ")

# popitem dictionary
data_terakhir = teman.popitem()
print(f"data terakhir : {data_terakhir}")

print(f"data teman : {teman}")