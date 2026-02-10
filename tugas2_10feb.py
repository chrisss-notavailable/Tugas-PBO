x = []

for i in range (10):
    y = int(input (f"masukkan angka ke {1+i}: "))
    x.append(y)

    genap = 0
    ganjil = 0
    
    for y in x :
        if (y%2==0):
            genap +=1
        else :
            ganjil+=1

print(f"rata-rata adalah :{sum(x)/len(x)}")
print(f"yang terbesar :{max(x)}")
print(f"yang terkecil :{min(x)}")
print(f"angka genap :{genap}")
print(f"angka ganjil :{ganjil}")