print("===== Selamat datang di XXV ====")
input("masukan tanggal hari ini: ")

print("== Berikut genre film yang tersedia ==")
print("1. horror")
print("2. action")

genre=int(input("silahkan memilih mau nonton film bergenre apa: "))

if(genre==1) :
    print("== Berikut film horror yang sedang tayang ==")
    print("1. the devil's light")
    print("2. pengabdi setan")

    int(input("silahkan pilih mau menonton film apa : "))
    int(input("mau memesan tiket sebanyak :"))
    print("total yang harus dibayar adalah Rp. 73.000")
elif(genre==2) :
    print("== Berikut film action yang sedang tayang ==")
    print("1. Black panther: wakanda forever")
    print("2. Avatar: the way of water")

    int(input("silahkan pilih mau menonton film apa : "))
    int(input("mau memesan tiket sebanyak :"))
    print("total yang harus dibayar adalah Rp. 237.500")
else:
    print("pilihan yang anda pilih tidak tersedia di bioskop ini")