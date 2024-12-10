#Flask

#Ir viegls un elastīgs Python tīmekļa ietvars - tīmekļa lietotņu veidošanai

from flask import Flask

app = Flask(__name__) #Izveido Flask lietotni

@app.route('/') #Definē galveno maršruts
def home():
    return "Hello, World!"

@app.route('/citsTeksts') #Definē otro maršrutu
def citsTeksts():
    return "Hey, šeit ir vēl viena lapa!"

@app.route('/sutit/<vards>') #Definē otro maršrutu
def sutit(vards):
    print(vards)
    return "Hey, ",vards

app.run()
