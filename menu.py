#!/usr/bin/python

def Nilai1():
    nilai = raw_input("Masukkan Nilai Awalnya : ")
    nilai = int(nilai)
    return nilai

def Nilai2():
    nilai = raw_input("Masukkan Nilai Akhirnya : ")
    nilai = int(nilai)
    return nilai

def Penjumlahan():
    print "Menu Penjumlahan "
    hasil = Nilai1()+Nilai2()
    return hasil

def Pengurangan():
    print "Menu Pengurangan "
    hasil = Nilai1()-Nilai2()
    return hasil

def Pembagian():
    print "Menu Pembagian "
    hasil = Nilai1()/Nilai2()
    return hasil

def Perkalian():
    print "Menu Perkalian "
    hasil = Nilai1()*Nilai2()
    return hasil

def Menu():
    print "1. Penjumlahan "
    print "2. Pengurangan "
    print "3. Pembagian "
    print "4. Perkalian "
    print
    menu = raw_input("Silahkan pilih salah satu menu : ")
    menu = int(menu)
    if menu == 1:
        print
        print Penjumlahan()
        print
        Menu()
    elif menu == 2:
        print
        print Pengurangan()
        print
        Menu()
    elif menu == 3:
        print
        print Pembagian()
        print
        Menu()
    elif menu == 4:
        print
        print Perkalian()
        print
        Menu()
    else :
        print "Menu belum terdaftar !"
Menu()

