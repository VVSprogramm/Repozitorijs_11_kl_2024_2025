"""
Izveido programmu, kas izdrukā informatīvu tekstu, pieprasa lietotāja ievadītus datus,
izveido jaunu objektu no datiem un klases Rekins un tad izmanto objekta metodi
izdrukat(), lai izvadītu rēķinu uz ekrāna!
"""

import ladite_OOP

print("Sveicināti! Šī programma izveido rēķinus koka lādīšu pasūtījumiem.")

klients = input("Ievadiet klienta vārdu: ")
veltijums = input("Ievadiet veltījuma tekstu: ")

platums = int(input("Ievadiet lādītes platumu (mm): "))
garums = int(input("Ievadiet lādītes garumu (mm): "))
augstums = int(input("Ievadiet lādītes augstumu (mm): "))

materiala_cena = float(input("Ievadiet kokmateriāla cenu (EUR/m2): "))

reikuns = ladite_OOP.Rekins(klients,veltijums,[platums,garums,augstums],materiala_cena)
reikuns.izdrukat()
