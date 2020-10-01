berat = float(input("Masukkan beraddd = "))
tinggi = float(input("Masukkan tinggi = "))
hasil = berat/((tinggi/100)**2)
if hasil < 18.5:
    print("Berat badan kurang")
elif 18.5 <= hasil <= 22.9:
    print("Berat badan normal")
elif 23 <= hasil <= 29.9:
    print("Berat badan berlebih")
elif hasil > 30:
    print("Obesitas")
else:
    print("Inputan salah")