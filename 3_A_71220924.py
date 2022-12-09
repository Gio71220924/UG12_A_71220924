a = int(input("Masukan pembatas:"))
b = int(input("Masukan angka yang dilarang:"))

for i in range(a):
    if i == b:
        continue
    else:
        print(i,end=" ")
