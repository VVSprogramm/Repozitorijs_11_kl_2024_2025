import csv
import datetime
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
        self.laiks = datetime.datetime.now()

    """
    Klasei Rekins pievieno metodi izdrukat(), kas izvada uz ekrāna glīti noformētu
    informāciju par rēķinu!
    """

    """
    Uzlabo klases Rekins metodi izdrukat(), lai tā drukātu arī aprēķināto apmaksas summu no
    metodes aprekins()!
    """

    """
    Papildini programmu, lai tā izsauc metodi saglabat() pirms rēķina izdrukāšanas!
    """
    def izdrukat(self):
        #self.saglabat()
        print("klienta vārds:",self.klients)
        print("veltijums:",self.veltijums)
        print("izmērs(platums, garums. augstums):",self.izmers)
        print("materiāla cena m2:",self.materials)
        print("Rekina summa:",self.aprekins())
        print("Laiks:",self.laiks)

    """
    Klasei Rekins pievieno metodi aprekins(), kas pēc dotās formulas un rēķina īpašībām
    aprēķina apmaksājamo summu! Metodi aprekins() izsauc, inicializējot objektu!
    """
    def aprekins(self):
        darba_samaksa = 15
        PVN = 21
        veltijuma_garums = len(self.veltijums)

        produkta_cena = (veltijuma_garums * 1.2) + ((self.izmers[0] * self.izmers[1] * self.izmers[2]) / 100 ) / 3 *self.materials
        PVN_summa = (produkta_cena + darba_samaksa) * PVN / 100
        rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa
        
        return rekina_summa

    """
    Papildini klasi Rekins ar metodi saglabat(), kas saglabā rēķina datus CSV datnē, kuras
    nosaukumsveidots no klienta vārda un datuma!
    """

    def saglabat(self):
        kolonnuNosaukumi = ['Vārds','Vēltījums','Izmēri','Materiāla_cena','rekina_summa','laiks']

        saturs = [self.klients,self.veltijums,self.izmers,self.materials,self.aprekins(),self.laiks]

        with open("csv_rekins.csv","a", encoding="UTF-8") as fails:
            csvwrite = csv.writer(fails) #Objekta izveide
            csvwrite.writerow(kolonnuNosaukumi)
            csvwrite.writerow(saturs)
