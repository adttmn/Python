print()
print("----------------------------------------")
print("           GEROBAK FRIED CHICKEN        ")
print("----------------------------------------")
print("Kode     Jenis potong            Harga")
print("----------------------------------------")
print("D            Dada                Rp. 2500")
print("P            Paha                Rp. 2000")
print("S            Sayap               Rp. 1500")
print()
banyak_jenis = int(input("Banyak Jenis : "))
kode_potong = []
banyak_potong = []
jenis_potong = []
harga = []
jumlah = []

i= 0
while i<banyak_jenis:
    print("Jenis Ke - ", i+1)
    kode_potong.append(input("Kode Potong [D/P/S] : "))
    banyak_potong.append(int(input("Banyak Potong : ")))
    print()

    if kode_potong[i] == "D" or kode_potong[i] == "d" :
        jenis_potong.append("Dada")
        harga.append("2500")
        jumlah.append(banyak_potong[i]*int("2500"))
    elif kode_potong[i] == "P" or kode_potong[i] == "p" :
        jenis_potong.append("Paha")
        harga.append("2000")
        jumlah.append(banyak_potong[i]*int("2000"))
    elif kode_potong[i] == "S" or kode_potong[i] == "s" :
        jenis_potong.append("Sayap")
        harga.append("1500")
        jumlah.append(banyak_potong[i]*int("1500"))
    else :
        jenis_potong.append("Kode Salah")
        harga.append("0")
        jumlah.append(banyak_potong[i]*int("0"))     
        print()
    i= i + 1
print()
print("            G E R O B A K  F R I E D              ")
print("                  C H I C K E N                   ")
print("--------------------------------------------------")
print("No.  Jenis        Harga        Banyak    Jumlah")
print("     Potong       Satuan       Beli      Harga ")
print("--------------------------------------------------")

a = 0
while a < banyak_jenis:
    print("%i    %s         %s          %i        Rp. %i" % (a+1,jenis_potong[a], harga[a], banyak_potong[a], jumlah[a]))
    a = a + 1
print("--------------------------------------------------")
sum=0
for each in jumlah:
    sum=sum+each
jumlah_bayar=sum
pajak = jumlah_bayar * 0.1 
total_bayar = jumlah_bayar + pajak
print("\t\t\t    Jumlah bayar Rp.", jumlah_bayar)
print("\t\t\t    Pajak 10 %   Rp.", pajak)
print("\t\t\t    Total Bayar  Rp.", total_bayar)
uang=int(input("\t\t\t    Uang Tunai   Rp. "))
kembalian=int(uang-total_bayar)
print("-----------------------------------------------------")
print("\t\t\t    Kembalian    Rp.",kembalian)
print("-----------------------------------------------------")
print("------------- T E R I M A  K A S I H ----------------")
print("--------- S U D A H  B E R B E L A N J A ------------")
print("-----------------------------------------------------")







