# program list buku

list_buku = []
while True:
    print("data buku")

    judul = input("masukan judul buku \t: ")
    penulis = input("masukan nama penulis \t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("\n")

    print("no. \t| judul \t| penulis")

    for index,buku in enumerate(list_buku):
        print(f"{index} \t| {buku[0]} \t| {buku[1]}" )

    isLanjut = input("apakah mau lanjut? (y/n) : ")

    if isLanjut == "n":
        break
