"""
Uzdevums: 
Izveidot klasi BankAccount, kas apraksta bankas kontu ar šādām īpašībām un metodēm:
Īpašības:
owner: konta īpašnieka vārds.
balance: konta bilance.
account_type: konta tips (piemēram, "krājkonts" vai "norēķinu konts").
Metodes:
deposit(amount): pievieno kontam naudas summu amount un izvada ziņojumu par bilanci.
withdraw(amount): noņem konta naudas summu amount, ja pietiekama bilance, un izvada ziņojumu; citādi izvada ziņu par nepietiekamu bilanci.
Izveido atbilstošu objektu un pārbaudi visu klasē iekļauto metožu darbību.

"""

class BankAccount():

    def __init__(self,owner,balance,account_type):
        self.owner = owner
        self.balance = balance
        self.account_type = account_type

    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return self.balance
        else:
            return "Nav pietiekami daudz līdzekļu kontā"
        
objekts1 = BankAccount("Anna",50,"Norēķinu karte")

print(objekts1.deposit(5))
print(objekts1.withdraw(50))
print(objekts1.withdraw(10))
