#Halaman 17 Modul Praktikum Pemrograman
#Created by Nadine Viga Septira 2270231043

# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")


#Celcius
celcius = float(input('Masukan suhu dalam celcius : '))
print("suhu adalah",celcius,"Celcius")


#Reamur
reamur = (4/5)*celcius
print("suhu dalam reamur adalah",reamur,"Reamur")


#Fahrenheit
fahrenheit = ((9/5)*celcius+32)
print("suhu dalam fahrenheit adalah",fahrenheit,"Fahrenheit")


#Kelvin
kelvin = celcius+273
print("suhu dalam kelvin adalah",kelvin,"Kelvin")