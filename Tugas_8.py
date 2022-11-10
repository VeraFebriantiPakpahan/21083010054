# Import library
from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(i):
   if (i+1)%2==0:
      print(i+1, "genap - ID Process", getpid())
   else:
     print(i+1, "ganjil - ID Process", getpid())
   sleep(1)

n=int(input("Input batasan : "))

# Sekuensial
print("sekuensial")
sekuensial_awal = time()
for i in range(n):
    cetak(i)
sekuensial_akhir = time()
print()

# Multiprocessing.Process
print("multiprocessing.Process")
kumpulan_proses = []
process_awal = time()
for i in range(n):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()
for i in kumpulan_proses:
    p.join()
process_akhir = time()
print()

# Multiprocessing.Pool
print("multiprocessing.Pool")
pool_awal = time()
pool = Pool()
pool.map(cetak, range(0,n))
pool.close()
pool_akhir = time()
print()

# Bandingkan waktu eksekusi
print("Waktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal,"detik")
print("Waktu multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu multiprocessing.Pool :", pool_akhir - pool_awal, "detik")
