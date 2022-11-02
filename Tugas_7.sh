#!/bin/bash

# Mendeklarasikan fungsi
panjang() {
       echo "Masukan Panjang :"
       read p

}
lebar() {
       echo "Masukan Lebar :"
       read l

}
luas() {
       echo "Menghitung Luas Bidang Persegi"
       panjang
       lebar
       let l=$p*$l
       echo "Luas Persegi :
$l"
}

# Memanggil fungsi
luas

