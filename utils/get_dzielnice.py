

import requests

# create new csv file to write later
import pandas as pd


df = pd.read_excel('../pkgs/spoldzielnie/spoldzielnie/dane/spoldzielnie_3.ods',dtype=str, header=0)

        #print(df.head())
with open("../pkgs/spoldzielnie/spoldzielnie/dane/spoldzielnie_dzielnice.csv", "w") as f:
    for index, row in df.iterrows():
        krs = row['krs']
        szer = row['szerokosc_geo']
        dlug = row['dlugosc_geo']
        reverse = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={szer}&lon={dlug}"

        a = requests.get(reverse)
    
        if a.status_code == 200:
            #print(a.json()['address']['suburb'])
            dzielnica = a.json()['address']['suburb']

            print(f"{krs},{dzielnica}")

            f.write(f"{krs},{dzielnica}\n")