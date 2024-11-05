#Objekt-orientēta programmēšana

#Objekts
#Klase

#class - atslēgas vārds klases izveidei

#īpašības

class Transportlidzeklis():

    #incializēšana
    def __init__(self,krasa,riepu_skaits,brauksanas_atrums,vietu_skaits):
        self.krasa = krasa
        self.riepu_skaits = riepu_skaits
        self.brauksanas_atrums = brauksanas_atrums
        self.vietu_skaits = vietu_skaits

    def dati(self):
        print(self.krasa)
        print(self.riepu_skaits)
        print(self.brauksanas_atrums)
        print(self.vietu_skaits)

bmw = Transportlidzeklis("Sarkana",4,240,5)
print(bmw.riepu_skaits)

bmw.dati()


#1.uzd.

#Izveido klasi Putns ar īpašībām krāsa, vide, kur dzīvo, lido (jā,nē)

class Putns():

    def __init__(self,krasa,vide,lido):
        self.krasa = krasa
        self.vide = vide
        self.lido = bool(lido)


#2.uzd.

#Izveido objektu (kādu piemēra puntu), piedēvē tam nepieciešamās īpašības

Erglis = Putns("Melns","Mežš, jūras krasts",True)

#3.uzd.

#Izvadi visas trīs objekta īpašības, izmantojot OOP

print(Erglis.krasa)
print(Erglis.vide)
print(Erglis.lido)
