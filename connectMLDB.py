#!/usr/bin/env python3
# Script para crear tabla, cargar csv con datos de prueba, grabarlos y leerlos 
# Solicitado por Voolkia para ML
# Sergio Arreguez -Wed 03 Feb 2021 11:57:37 AM -03 arreguez@yahoo.com
#############################################################################


import sqlite3
import csv

conn = sqlite3.connect('baseML.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS PRODUCTOS
                 (SELLER_ID integer, 
                  SITE_ID text, 
                  ITEM_ID integer, 
                  TITLE_ITEM text, 
                  CATEGORY_ID integer, 
                  NAME text )""")


# Inserto algunos datos desde un CSV.
with open('dataML.csv','r') as datosML: 
    datos_a_cargar = csv.DictReader(datosML) 
    for i in datos_a_cargar:
       #print (f"row {i}")
       arrayDB = [(i['SELLER_ID'], i['SITE_ID'], i['ITEM_ID'], i['TITLE_ITEM'], i['CATEGORY_ID'], i['NAME'])]
       cursor.executemany("INSERT INTO PRODUCTOS ( \
                                       SELLER_ID, SITE_ID, ITEM_ID, TITLE_ITEM, CATEGORY_ID, NAME)  \
                                       VALUES (?, ?, ?, ?, ?, ?);", arrayDB)

conn.commit()

seller = int( input("Seller?  (Enter=179571326):") or 179571326)
siteid = input("Site ID? (Enter=MLA): ") or "MLA"

query = "SELECT SELLER_ID, TITLE_ITEM, CATEGORY_ID, NAME \
         FROM PRODUCTOS WHERE SELLER_ID = {} AND SITE_ID == '{}'".format(seller, siteid)


productos = cursor.execute(query).fetchall()

with open ("output.txt","w") as OUTPUT:
   OUTPUT.write ("    ID        TITLE    CATEGORY_ID   NAME\n")
   OUTPUT.write ("=========================================\n")

   for registro in productos:
      Values =  str((registro[0], registro[1], registro[2], registro[3]))
      OUTPUT.write (Values)
      OUTPUT.write ('\n')

conn.close()
