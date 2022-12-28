import os
import sys

print("+=======================================================+");
print("|\tSELAMAT DATANG DI MESIN HITUNG HASIL PANEN\t|");
print("|-------------------------------------------------------|");
print("|\tMenghitung Hasil Panen Padi dengan Akurat\t|");
print("+=======================================================+");
print("|\tNo     |     Jenis Padi      |      Harga\t|")
print("|_______________________________________________________|");
print("|\t1      |     Padi ketan      |       5000\t|")
print("|\t2      |     Padi wangi      |      15000\t|")
print("|\t3      |     Padi pulen      |      12000\t|")
print("|\t4      |     Padi gogo       |      18000\t|")
print("|\t5      |     Padi rawa       |       7000\t|")
print("|_______________________________________________________|");

#proses input
pilihan = int(input("|\tPilih jenis padi        : "))

if pilihan == 1 :
  jumlah = int(input("|\tJumlah pemanenan(kg)    : "))
  modal = int(input("|\tModal awal              : Rp "))
  total = jumlah * 5000
  print("|\tTotal penjualan adalah  : Rp ",total)
  untung = total - modal
  print("|\tHasil keuntungan        : Rp ",untung)
  print("|____________________________________________________");
  if total >= modal :
    print("|\t\tPanen anda sukses\t\t\t|")
  elif untung == 0 :
    print("| Panen tidak menghasilkan, coba lagi dengan cara baru  |")
  else :
    print("|\tPanen anda gagal, silakan coba bertani lagi\t|")

elif pilihan == 2 :
  jumlah = int(input("|\tJumlah pemanenan(kg)    : "))
  modal = int(input("|\tModal awal              : Rp "))
  total = jumlah * 15000
  print("|\tTotal penjualan adalah  : Rp ",total)
  untung = total - modal
  print("|\tHasil keuntungan        : Rp ",untung)
  print("|___________________________________________________");
  if total >= modal :
    print("|\t\tPanen anda sukses\t\t\t|")
  elif untung == 0 :
    print("| Panen tidak menghasilkan, coba lagi dengan cara baru  |")
  else :
    print("|\tPanen anda gagal, silakan coba bertani lagi|")

elif pilihan == 3 :
  jumlah = int(input("|\tJumlah pemanenan(kg)    : "))
  modal = int(input("|\tModal awal              : Rp "))
  total = jumlah * 12000
  print("|\tTotal penjualan adalah  : Rp ",total)
  untung = total - modal
  print("|\tHasil keuntungan        : Rp ",untung)
  print("|__________________________________________________");
  if total >= modal :
    print("|\t\tPanen anda sukses\t\t\t|")
  elif untung == 0 :
    print("| Panen tidak menghasilkan, coba lagi dengan cara baru  |")
  else :
    print("|\tPanen anda gagal, silakan coba bertani lagi|")

elif pilihan == 4 :
  jumlah = int(input("|\tJumlah pemanenan(kg)    : "))
  modal = int(input("|\tModal awal              : Rp "))
  total = jumlah * 18000
  print("|\tTotal penjualan adalah  : Rp ",total)
  untung = total - modal
  print("|\tHasil keuntungan        : Rp ",untung)
  print("|__________________________________________________");
  if total >= modal :
    print("|\t\tPanen anda sukses\t\t\t|")
  elif untung == 0 :
    print("| Panen tidak menghasilkan, coba lagi dengan cara baru  |")
  else :
    print("|\tPanen anda gagal, silakan coba bertani lagi |")

elif pilihan == 5 :
  jumlah = int(input("|\tJumlah pemanenan(kg)    : "))
  modal = int(input("|\tModal awal              : Rp "))
  total = jumlah * 7000
  print("|\tTotal penjualan adalah  : Rp ",total)
  untung = total - modal
  print("|\tHasil keuntungan        : Rp ",untung)
  print("|_________________________________________________");
  if total >= modal :
    print("|\t\tPanen anda sukses\t\t\t")
  elif untung == 0 :
    print("| Panen tidak menghasilkan, coba lagi dengan cara baru  |")
  else :
    print("|\tPanen anda gagal, silakan coba bertani lagi")
print("+=======================================================+");
