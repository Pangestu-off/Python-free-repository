import tkinter as graphic

main = graphic.Tk()

def isi():
    print("Nama Depan : %s\nNama Belakang : %s"% (kotak.get(), kotak2.get()))

def keluar():
    exit()

teks = graphic.Label(text = "Masukkan Nama Depan di Baris Kotak Pertama dan \n Nama Belakang di Baris Kotak Kedua")

kotak = graphic.Entry()
kotak2 = graphic.Entry()

tombol = graphic.Button(text = "Menampilkan di dalam Terminal", 
foreground = "black", 
background = "white",
command =  isi
)

keluar = graphic.Button(text = "keluar dari graphic", 
foreground = "black", 
background = "white",
command = keluar
)
teks.pack()
kotak.pack()
kotak2.pack()
tombol.pack()
keluar.pack()
main.mainloop()