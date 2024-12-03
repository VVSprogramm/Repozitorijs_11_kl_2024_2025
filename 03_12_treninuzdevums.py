import requests
import PySimpleGUI as sg
from bs4 import BeautifulSoup

# Funkcija, kas nolasa datus no mājaslapas
def fetch_data(values):
    url = values
    
    response = requests.get(values)
    # response.raise_for_status()  # Pārbauda, vai nav kļūdu
    return response.text
    
def find_smth(find,values):
    response = requests.get(values)
    apstradajamais_teksts = BeautifulSoup(response.content, 'html.parser')

    izvade = apstradajamais_teksts.find(class_= find).get_text()
    #rezultats = izvade[1]#.find(find)#.get_text()
    return izvade

#find_smth('p','https://vvsprogramm.github.io/A/')
# Izveido lietotāja saskarni
layout = [
    [sg.Text("Mājaslapas URL:"), sg.InputText(key='-URL-', size=(50, 1))],
    [sg.Button("Nolasa datus", key='-FETCH-')],
    # [sg.Text(key='-OUTPUT-')]
    [sg.Multiline(size=(80, 20), key='-OUTPUT-')],
    [sg.Text("Atrast"), sg.InputText(key=('find'))],
    [sg.Button("Nolasa datus", key='-Meklet-')],
    [sg.Text(key='-OUTPUT2-')]
]

window = sg.Window("Mājaslapas datu nolasītājs", layout)

# Lietotāja saskarnes notikumu apstrāde
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-FETCH-':
        data = fetch_data(values['-URL-'])
        if data:
            window['-OUTPUT-'].update(data)
    elif event == '-Meklet-':
        data = find_smth(values['find'],values['-URL-'])
        window['-OUTPUT2-'].update(data)
window.close()
