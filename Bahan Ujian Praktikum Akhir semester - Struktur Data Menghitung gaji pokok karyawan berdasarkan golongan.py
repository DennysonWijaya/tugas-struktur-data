#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Program untuk menghitung gaji pokok karyawan berdasarkan golongan 
#Program di buat oleh Dennyson Wijaya
#NIM : 2220113955
#Program Studi : Sistem Informasi
#Semester: 2
#Kelas : M-1
#Mata Kuliah : Struktur Data
#Nama Dosen : Wilianto Gan
# Bahan Ujian Praktikum Akhir semester - Struktur Data
#Jenis Ujian : UAS


# # Menghitung gaji pokok karyawan berdasarkan golongan

# In[ ]:


def hitung_gaji(golongan, jam_kerja):
    gaji_pokok = {
        "A": 10000000,
        "B": 7000000,
        "C": 5000000,
        "D": 3000000
    }
    
    if golongan in gaji_pokok:
        if jam_kerja <= 40:
            gaji_total = gaji_pokok[golongan]
        else:
            gaji_lembur = (jam_kerja - 40) * (gaji_pokok[golongan] / 40) * 1.5
            gaji_total = gaji_pokok[golongan] + gaji_lembur
        return gaji_total
    else:
        return None

while True:
    print("Selamat datang di Kalkulator Gaji Karyawan")
    golongan = input("Masukkan golongan (A, B, C, D): ")
    jam_kerja = int(input("Masukkan jam kerja per bulan: "))

    gaji = hitung_gaji(golongan, jam_kerja)
    if gaji is not None:
        print("===========================================")
        print("Hasil perhitungan gaji karyawan:")
        print(f"Golongan: {golongan}")
        print(f"Jam Kerja: {jam_kerja} jam/bulan")
        print(f"Gaji Total: Rp {gaji}")
        print("===========================================")
        break
    else:
        print("Maaf, golongan yang Anda masukkan tidak valid. Silakan coba lagi.")

