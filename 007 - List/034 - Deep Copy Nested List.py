# data    index[0]
data_0 = [1,2,3,4,]
# data    index[1]
data_1 = [5,6,7,8,]

# data    index[0] index[1]
data_2d = [data_0,data_1]
data_2d_copy = data_2d.copy()

print(f"data nested asli : {data_2d}")
print(f"data nested copy : {data_2d_copy}")

# mengambil data dengan index
data = data_2d[0][1] # tentukan index
print(f"mengambil dengan index : {data}")

# address
print(f"data address asli : {hex(id(data_2d))}") 
print(f"data address copy : {hex(id(data_2d_copy))}") 