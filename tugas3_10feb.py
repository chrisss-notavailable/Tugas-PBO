depan=str(input("masukkan nama depan : "))
belakang=str(input("masukkan nama belakang : "))

x=[depan,belakang]
lengkap = x[0] + ' ' + x[1]

print(f"nama lengkap :{lengkap}")
print(f"nama dibalik :{lengkap[::-1]}")