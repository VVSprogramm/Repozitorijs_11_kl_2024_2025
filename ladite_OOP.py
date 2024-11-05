print("Sveicināti! Šī programma izveido rēķinus koka lādīšu pasūtījumiem.")

klients = input("Ievadiet klienta vārdu: ")
veltijums = input("Ievadiet veltījuma tekstu: ")

platums = int(input("Ievadiet lādītes platumu (mm): "))
garums = int(input("Ievadiet lādītes garumu (mm): "))
augstums = int(input("Ievadiet lādītes augstumu (mm): "))

materiala_cena = float(input("Ievadiet kokmateriāla cenu (EUR/m2): "))


darba_samaksa = 15
PVN = 21
veltijuma_garums = len(veltijums)

produkta_cena = (veltijuma_garums * 1.2) + ((platums * garums * augstums) / 100 ) / 3 *materiala_cena
PVN_summa = (produkta_cena + darba_samaksa) * PVN / 100
rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa

print(produkta_cena)
print(rekina_summa)


"""
Izveido klasi Rekins, kas saņem 4 parametrus un izveido attiecīgas īpašības ar dotajiem lielumiem:
● klients (simbolu virkne);
● veltijums (simbolu virkne);
● izmers (masīvs ar 3 veseliem skaitļiem);
● materials (decimāldaļa)!
"""

class Rekins():
    def __init__(self,klients, veltijums, izmers, materials):
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = materials

"""
Klasei Rekins pievieno metodi izdrukat(), kas izvada uz ekrāna glīti noformētu
informāciju parrēķinu!

Klasei Rekins pievieno metodi aprekins(), kas pēc dotās formulas un rēķina īpašībām
aprēķinaapmaksājamo summu! Metodi aprekins() izsauc, inicializējot objektu!

Uzlabo klases Rekins metodi izdrukat(), lai tā drukātu arī aprēķināto apmaksas summu no
metodes aprekins()!

Izveido programmu, kas izdrukā informatīvu tekstu, pieprasa lietotāja ievadītus datus,
izveido jaunu objektu no datiem un klases Rekins un tad izmanto objekta metodi
izdrukat(), lai izvadīturēķinu uz ekrāna!

Papildini klasi Rekins ar metodi saglabat(), kas saglabā rēķina datus CSV datnē, kuras
nosaukumsveidots no klienta vārda un datuma!

Papildini programmu, lai tā izsauc metodi saglabat() pirms rēķina izdrukāšanas!"""
