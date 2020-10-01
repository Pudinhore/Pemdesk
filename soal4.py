n = int(input("Berapa angka? "))
tempat = []
for i in range(n):
    tempat.append(int(input("Masukkan angka ke{} = ".format(i))))
print("Nilai maksimal = {}".format(max(tempat)))
print("Nilai minimal = {}".format(min(tempat)))