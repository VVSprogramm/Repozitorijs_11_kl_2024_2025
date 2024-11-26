#API - apllication programming interface
#Komunikācijas nodrošināšana

import requests
from bs4 import BeautifulSoup

lapa = requests.get("https://data.gov.lv/lv")
# print(lapa.text)

apstradajamais_teksts = BeautifulSoup(lapa.content, 'html.parser')

banera_teksts = apstradajamais_teksts.find_all(class_ = "region region-hero")[0].get_text()
print(banera_teksts)
