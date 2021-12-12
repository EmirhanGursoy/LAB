# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 21:32:35 2021

@author: emirg
"""
#MAP FONKSIYONU ORNEK
def asal(sayi):
    asalMi = True
    for i in range(2,sayi):
        if sayi % i == 0:
            asalMi = False
            break
    if asalMi == False:
        print("Sayi asal degildir. ")
    else:
        print("Sayi asaldir.")
        
map(asal,[3,5,6,7,8,9,11,45,67])
list(map(asal,[3,5,6,7,8,9,11,45,67]))
            
    