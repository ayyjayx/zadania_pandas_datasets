import pandas as pd
import numpy as np
import xlrd
import openpyxl

#Zad 1
df = pd.read_excel('imiona.xlsx')
print(df)

# Zad 2
# podpunkt 1
# print(df[df['Liczba']<1000])
# podpunkt 2
# print(df[df['Imie']=='ALAN'])
# podpunkt 3
# print("Ilosc urodzonych dzieci wynosi:",df['Liczba'].sum())
# podpunkt 4
# df2 = (df[((df.Rok >= 2005) & (df.Rok <= 2010))])
# print("Ilosc urodzonych dzieci w latach 2005-2010 wynosi:",df2['Liczba'].sum())
# podpunkt 5
# df3 = (df[((df.Rok == 2000) & (df.Plec == 'M'))])
# print("Ilosc urodzonych chlopcow w roku 2000 wynosi:",df3['Liczba'].sum())
# podpunkt 6

# podpunkt 7
df4 = (df[(df.Plec == 'K')]) & df.sort_values(by='Liczba', ascending=False)
# df5 = df.sort_values(by='Liczba', ascending=False)
#print('Najbardziej popularnie imie damskie to:', df5['Imie'], 'a meskie:', df4['Imie'])
print(df4)
