import PySimpleGUI as sg  #Vizuālās saskarnes bibliotēka
import ladite_OOP as ladite

#Funkcijas, klases
#Failā ladite_OOP.py

#Lietotāja saskarne priekš programmas Lādīte

sg.theme('DarkAmber') #Saskarnes tēma
#Izkārtojums saskarnei
layout = [[sg.Text("Sveicināti! Šī programma izveido rēķinus koka lādīšu pasūtījumiem.")],
          [sg.Text('Vārds'),sg.InputText()],
          [sg.Text('Veltījums'),sg.InputText()],
          [sg.Text('Augstums'),sg.InputText()],
          [sg.Text('Platums'),sg.InputText()],
          [sg.Text('Garums'),sg.InputText()],
          [sg.Text('Materiāla cena m2'),sg.InputText()],
          [sg.Button("Parādīt rēķinu konsolē"),sg.Button("Saglabāt rēķinu")]
          ]

window = sg.Window('Rēķinu izveide lādīšu pasūtījumiem',layout) #Loga izveide

while True: #Saskarnes darbības cikls
    event, values = window.read() #Notikumu un vērtību pārbaude
    rekins = ladite.Rekins(values[0],values[1],[int(values[3]),int(values[4]),int(values[2])],int(values[5])) #Objekta izveide
    if event == "Parādīt rēķinu konsolē": #Kas notiek, ja nospiež pogu parādīt rēķinu konsolē
        rekins.izdrukat() #Metodes izdrukāt pasaukšana
    if event == "Saglabāt rēķinu": #Kas notiek, ja nospiež pogu Saglabāt rēķinu
        rekins.saglabat() #Metodes saglabāt pasaukšana
    if event == sg.WINDOW_CLOSED:  #Ja aizver lodziņu
        break #Iziešana no cikla

window.close()
