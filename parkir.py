print("")
print("=========== P E M B A Y A R A N  P A R K I R ===========")
print("")

from datetime import datetime
masuk =datetime(input("Masukkan Jam Masuk   : "))
keluar=datetime(input("Masukkan Jam Keluar  : "))
lama=keluar-masuk
payment=2000
print("Lama Parkir \t     : ", lama, "jam")
if lama <1:
    satu_jam_pertama=payment
    print("Biaya Parkir \t\t   : Rp.", satu_jam_pertama)
elif lama <10:
    biaya_selanjutnya = (lama-1)*2000+payment
    print("Biaya Parkir \t     : Rp.", biaya_selanjutnya)
elif lama >= 10:
    print("Biaya Parkir    :  Rp.", 20000)
else:
    print("nul")
    
print("\nTotal harus Dibayar  : Rp.",biaya_selanjutnya)
uang=int(input("Uang Tunai Pembeli   : Rp. "))
kembalian=int(uang-biaya_selanjutnya)
print("Kembalian :RP.",kembalian)

#Struk Parkir
print("\n============================================")
print("========== S T R U K   P A R K I R =========")
print("============================================")
print ("Jam Masuk\t\t:",{masuk})
print ("Jam Keluar\t\t:",{keluar})
print ("Harga 1 Jam Pertama\t: Rp.",payment)
print ("Lama Parkir\t\t:",lama,"Jam")
print ("Biaya Parkir\t\t: Rp.",biaya_selanjutnya)
print ("Dibayar\t\t        : Rp.",uang)
print ("Kembalian\t\t: Rp.",kembalian)
print("============================================")
print("============================================")