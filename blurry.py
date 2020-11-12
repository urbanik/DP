pip install imutils
from imutils import paths
import argparse
import cv2

import numpy as np
from matplotlib import pyplot as plt

import pandas as pd
import os
import shutil #na kopirovanie suborov
import glob #na najdenie vsetkym jpeg suborov


#CAST PRVA PRIPRAVA

os.getcwd() #zistenie cesty k suboru
#os.chdir('c:\\Users\\katarinas\\desktop') #nastavenie novej cesty k suboru

data=pd.read_csv('c:\\Users\\katarinas\\desktop\\11.csv', header=None) #otvorenie a nacitanie csv suboru
data.head(1) #vypisanie prveho riadku
data.iloc[:10, ] #vypisanie prvych 10 riadkov (iloc metoda ktora dava riadky a stlpce do pozicie indexov)
len(data) #zistenie kolko riadkov ma dany dokument

    
#moznost prva riesenia problemu so vzdialenym servrom
os.chdir('\\\\metstor1.mstep\\meteo_data\\SESARDATA\\foto\\2018\\11') #namapovanie cesty na vzdialeny server riesime cez dve lomky alebo cez nalinkovanie serveru na nejaky prazdny disk
#fero = cv2.imread('fullhd-090-090-201811010500-01.png',0) #vykreslenie snimky

#skopirovanie fotiek z metstoru do zlozky "uloz"
uloz = 'c:\\Users\\katarinas\\desktop\\uloz'
for row in data[0]:
   shutil.copy(row, uloz)
   
print(data[0][10])  #vypisanie konkretneho riadku/stlpca
print(row)  
    

#moznost druha risenia problemu so vzdialenym serverom
#os.chdir('y:\\SESARDATA\\foto\\2018\\11\\11\\1240\\90_FULLHD') #nalinkovanie serveru na disk v pocitaci
#fero = cv2.imread('fullhd-090-000-201811111240-01.png',0)  #nacitanie obrazku
#plt.imshow(fero, cmap = 'gray') #zobrazenie obrazku



#CAST DRUHA samotny vypocet

fero = cv2.imread('h.png',0) #nacitanie obrazka
def variance_of_laplacian(img): #vypocet Laplacian variancie
	return cv2.Laplacian(img, cv2.CV_64F).var()  
variance_of_laplacian(fero)
plt.imshow(fero, cmap = 'gray')

os.chdir('c:\\Users\\katarinas\\Desktop\\uloz') #potrebujeme aby sme presli kazdy obrazok v zlozke kde sa nachadzaju a vypocitali k nemu jeho hodnotu 
zoznam_obrazkov = os.listdir()

for imagePath in zoznam_obrazkov:  
   if imagePath == '.DS_Store':
       continue
   #print(imagePath)
   image = cv2.imread(imagePath)
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   fm = variance_of_laplacian(gray)
   #zapisanie vysledkov do textaku
   f = open('C:\\Users\\katarinas\\Desktop\\uloz\\zapis.txt', "a") 
   f.write(imagePath+ ';' + str(fm) + '\n')
   f.close()
   
   
   
   #treba doplnit hranicu thresholdu a podla dohody ci bude alert vypisovany na obrazok alebo niekam interne


