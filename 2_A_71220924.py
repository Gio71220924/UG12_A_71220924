nama = str(input("Masukan nama:"))
i=0
k = 0
for i in nama:
    k = k+1
    print(nama[:k])

for i in nama:
    k = k-1
    print(nama[:k])
