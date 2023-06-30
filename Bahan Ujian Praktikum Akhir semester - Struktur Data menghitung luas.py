#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Program yang dapat menghitung Luas bangun berikut: trapesium, lingkaran, balok, segitiga, persegi panjang, dan persegi. 
#Program di buat oleh Dennyson Wijaya
#NIM : 2220113955
#Program Studi : Sistem Informasi
#Semester: 2
#Kelas : M-1
#Mata Kuliah : Struktur Data
#Nama Dosen : Wilianto Gan
# Bahan Ujian Praktikum Akhir semester - Struktur Data
#Jenis Ujian : UAS


# # Bahan Ujian Praktikum Akhir semester - Struktur Data

# In[ ]:


import math

class BangunDatar:
    def __init__(self):
        pass
    
    def luas_trapesium(self, alas, atas, tinggi):
        return ((alas + atas) * tinggi) / 2
    
    def luas_lingkaran(self, jari_jari):
        return math.pi * jari_jari ** 2
    
    def luas_balok(self, panjang, lebar, tinggi):
        return 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    
    def luas_segitiga(self, alas, tinggi):
        return (alas * tinggi) / 2
    
    def luas_persegi_panjang(self, panjang, lebar):
        return panjang * lebar
    
    def luas_persegi(self, sisi):
        return sisi ** 2

# Membuat objek dari kelas BangunDatar
bangun = BangunDatar()

# Contoh penggunaan program
print("Program Menghitung Luas Bangun Datar")
print("-----------------------------------")

# Memilih bangun datar
print("Pilih bangun datar:")
print("1. Trapesium")
print("2. Lingkaran")
print("3. Balok")
print("4. Segitiga")
print("5. Persegi Panjang")
print("6. Persegi")

pilihan = int(input("Masukkan pilihan (1-6): "))

if pilihan == 1:
    # Memasukkan nilai-nilai yang diperlukan untuk menghitung luas trapesium
    alas = float(input("Masukkan panjang alas: "))
    atas = float(input("Masukkan panjang atas: "))
    tinggi = float(input("Masukkan tinggi: "))

    # Memanggil fungsi untuk menghitung luas trapesium
    luas = bangun.luas_trapesium(alas, atas, tinggi)

    print("Luas trapesium adalah:", luas)

elif pilihan == 2:
    # Memasukkan nilai-nilai yang diperlukan untuk menghitung luas lingkaran
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))

    # Memanggil fungsi untuk menghitung luas lingkaran
    luas = bangun.luas_lingkaran(jari_jari)

    print("Luas lingkaran adalah:", luas)

elif pilihan == 3:
    # Memasukkan nilai-nilai yang diperlukan untuk menghitung luas balok
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))

    # Memanggil fungsi untuk menghitung luas balok
    luas = bangun.luas_balok(panjang, lebar, tinggi)

    print("Luas balok adalah:", luas)

elif pilihan == 4:
    # Memasukkan nilai-nilai yang diperlukan untuk menghitung luas segitiga
    alas = float(input("Masukkan panjang alas: "))
    tinggi = float(input("Masukkan tinggi: "))

        # Memanggil fungsi untuk menghitung luas segitiga
    luas = bangun.luas_segitiga(alas, tinggi)

    print("Luas segitiga adalah:", luas)

elif pilihan == 5:
    # Memasukkan nilai-nilai yang diperlukan untuk menghitung luas persegi panjang
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))

    # Memanggil fungsi untuk menghitung luas persegi panjang
    luas = bangun.luas_persegi_panjang(panjang, lebar)

    print("Luas persegi panjang adalah:", luas)

elif pilihan == 6:
    # Memasukkan nilai-nilai yang diperlukan untuk menghitung luas persegi
    sisi = float(input("Masukkan panjang sisi persegi: "))

    # Memanggil fungsi untuk menghitung luas persegi
    luas = bangun.luas_persegi(sisi)

    print("Luas persegi adalah:", luas)

else:
    print("Pilihan yang Anda masukkan tidak valid.")

