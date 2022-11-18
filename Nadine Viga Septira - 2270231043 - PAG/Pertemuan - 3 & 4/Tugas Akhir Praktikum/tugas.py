print("-----Nadine Viga Septira-------")
print("----------Cafe Gabut-----------")
print("----------2270231043-----------")

nama = input("Nama Pelanggan : ")
tanggal = input("Tanggal Pembelian :    ")
alamat = print("Jalan Raya Jatiwaringin, RT. 03 / RW. 04, Jatiwaringin, Pondok Gede, RT.009/RW.005, Jaticempaka, Kec. Pd. Gede, Kota Bks, Jawa Barat 13077s")
notelp = print("500600")
print("--------------------------------------") 
print("        ======== Menu ========        ")
print("--------------------------------------")
print("1. Red Velvet                Rp. 20000")
print("2. Matcha                    Rp. 20000")
print("3. Milkshake                 Rp. 18000")
print("4. Spaghetti                 Rp. 26000")
print("5. Steak Chicken Mushroom    Rp. 32000")
print("6. Dimsum                    Rp. 25000")
print("--------------------------------------")
h = []
a = 1

menu_pesanan = int(input("Masukan Menu Pesanan : "))
if menu_pesanan == 1:
   harga = 20000
elif menu_pesanan == 2:
   harga = 20000
elif menu_pesanan == 3:
   harga = 18000
elif menu_pesanan == 4:
   harga = 26000
elif menu_pesanan == 5:
   harga = 32000
elif menu_pesanan == 6:
   harga = 25000
else:
    while True:
        print("==== Menu tidak tersedia silahkan pilih menu lainnya ====") 
        if menu_pesanan == 1 or menu_pesanan == 2 or menu_pesanan == 3 or menu_pesanan == 5 or menu_pesanan == 6:
           if menu_pesanan == 1:
              harga = 20000
           elif menu_pesanan == 2:
              harga = 20000
           elif menu_pesanan == 3:
              harga = 18000
           elif menu_pesanan == 4:
              harga = 26000
           elif menu_pesanan == 5:
              harga = 32000
           elif menu_pesanan == 6:
              harga = 25000 
              break

jumlah_pembelian = int(input("Masukan Jumlah Pembelian : "))
for i in range(jumlah_pembelian):
    h.append(harga)

while True:
    jawab = input("Apakah ada yang ingin ditambah/dikurangi? tambah/kurang/n?")
    if jawab == 'tambah':
        tambah = int(input("Masukan Menu Pesanan :"))
        if tambah == 1:
           harga = 20000
        elif tambah == 2:
           harga = 20000
        elif tambah == 3:
           harga = 18000
        elif tambah == 4:
           harga = 26000
        elif tambah == 5:
           harga = 32000
        elif tambah == 6:
           harga = 25000 
        jumlah_tambahan = int(input("Masukan Jumlah Tambahan : "))
        for i in range(jumlah_tambahan):
            h.append(harga) 
        c = jumlah_tambahan + jumlah_pembelian
        print("Total Pesanan: ",c)
        bayar = sum(h)
        print("Total Pembayaran: Rp.{}",format(bayar))
        break

    elif jawab == 'kurang' : 
        kurang = int(input("Berapa jumlah yang ingin dikurangkan? : "))
        for i in range(kurang):
            if kurang <= 1:
                a -= kurang
                del h[a]
                bayar = sum(h)
                break
            else:
                kurang -= a
                del h[kurang]
                if kurang < 0:
                    break
        c = jumlah_pembelian - kurang
        print("Total Pemesanan: ",c)
        bayar = sum(h)
        print("Total Pembayaran: Rp.{}",format(bayar))
        break
    else:
        bayar = sum(h)
        c = jumlah_pembelian
        print("Total Pemesanan: ",c)
        print("Total Pembayaran: Rp.{}",format(bayar))
        break

