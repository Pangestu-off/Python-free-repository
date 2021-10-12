def menumaskapai():
    print("*********************")
    print("Menu Maskapai Pesawat")
    print("*********************")
    print("Pesan Tiket :")
    print("[1] Garuda Indonesia")
    print("[2] Lion Air")
    print("[3] EXIT")
    pilihan = input("Masukkan Pilihan :")
    if(pilihan == "1"):
        garuda()
    if(pilihan == "2"):
        Lionair()
    if(pilihan == "3"):
        exit()
    if(pilihan > "3"):
        menumaskapai()

def garuda():
    print("***********************")
    print("[1] Jakarta - BANDUNG")
    print("[2] BANDUNG - Jakarta")
    print("***********************")
    pembayaran()
  
def Lionair():
    print("*******************************")
    print("[1] Jakarta - Bandung")
    print("[2] Tanjung Pinang - Yogyakarta")
    print("*******************************")
    pembayaran()
     
           
def pembayaran():
    menuju = input("Pilih Tujuan :")
    if(menuju == "2"):
        print("Harga : Rp. 900.000") 
        harga = 900000
    if(menuju == "3"):
        print("Harga : Rp. 800.000")
        harga = 800000
    bayar = int(input("Masukkan Nominal Duit Anda :"))
    total = bayar - harga
    print("Uang Kembalian Anda : Rp.",total)
    menumaskapai()
    

if __name__ == "__main__":
    menumaskapai()
