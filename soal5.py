uname = "afifudin"
pwd = 20020704
i = 1
while True:
    getUname = input("Masukkan username = ")
    if getUname == uname:
        break
    else:
        print("Username tidak sama")
while i <= 3:
    getPwd = int(input("Masukkan password = "))
    if getPwd == pwd:
        print("Anda berhasil login")
        break
    else:
        print("Password salah")
    if i == 3:
        print("Username atau password salah, coba lagi nanti")
        break
    i += 1