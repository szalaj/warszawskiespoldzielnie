import requests

# create new csv file to write later
import pandas as pd


with open('../pkgs/spoldzielnie/src/spoldzielnie/dane/spoldzielnie_krs.txt', 'r') as f:
    data = f.read()
#     # get first line

# create new pandas dataframe
df = pd.DataFrame(columns=['nazwa', 'krs', 'nip', 'regon', 'adres', 'kod_pocztowy', 'miejscowosc', 'forma_prawna', 'data_rejestracji', 'szer', 'dlug'])

# create and open new csv file to write
with open('../pkgs/spoldzielnie/src/spoldzielnie/dane/spoldzielnie_krs_dane3.csv', 'w') as f:
    for i,krs in enumerate(data.split('\n')):
        if i !=0:
            print(krs)
            rejestr = 'P'
            x = requests.get(f"https://api-krs.ms.gov.pl/api/krs/OdpisAktualny/{krs}?rejestr={rejestr}&format=json")
            print(x.status_code)
            if x.status_code == 200:
                print(x)
                print(x.json()['odpis']['dane']['dzial1']['danePodmiotu'])
                print(x.json()['odpis']['dane']['dzial1']['siedzibaIAdres'])
                data_rejestracji = x.json()['odpis']['naglowekA']['dataRejestracjiWKRS']

                nazwa = x.json()['odpis']['dane']['dzial1']['danePodmiotu']['nazwa']
                forma_prawna = x.json()['odpis']['dane']['dzial1']['danePodmiotu']['formaPrawna']
                nip = x.json()['odpis']['dane']['dzial1']['danePodmiotu']['identyfikatory']['nip']
                regon = x.json()['odpis']['dane']['dzial1']['danePodmiotu']['identyfikatory']['regon']

                if 'ulica' in x.json()['odpis']['dane']['dzial1']['siedzibaIAdres']['adres']:
                    ulica = x.json()['odpis']['dane']['dzial1']['siedzibaIAdres']['adres']['ulica']
                else:
                    ulica = ''

                if 'nrDomu' in x.json()['odpis']['dane']['dzial1']['siedzibaIAdres']['adres']:
                    nr_domu = x.json()['odpis']['dane']['dzial1']['siedzibaIAdres']['adres']['nrDomu']
                else:
                    nr_domu = ''

                if 'nrLokalu' in x.json()['odpis']['dane']['dzial1']['siedzibaIAdres']['adres']:
                    nr_lokalu= x.json()['odpis']['dane']['dzial1']['siedzibaIAdres']['adres']['nrLokalu']
                else:
                    nr_lokalu = ''

                kod_pocztowy= x.json()['odpis']['dane']['dzial1']['siedzibaIAdres']['adres']['kodPocztowy']
                miejscowosc= x.json()['odpis']['dane']['dzial1']['siedzibaIAdres']['adres']['miejscowosc']

                adres_query = f"{ulica} {nr_domu} {miejscowosc}"

                # upper case adres_query
                adres_query = adres_query.upper()

                # convert adres_query to ascii url format

                adres_query = adres_query.replace('UL.', '')
                adres_query = adres_query.replace('AL.', '')
                adres_query = adres_query.replace('FR.', '')
                adres_query = adres_query.replace('R.MIELCZARSKIEGO', 'MIELCZARSKIEGO')
                adres_query = adres_query.replace('  ', ' ')
                adres_query = adres_query.replace(' ', '+')
                # adres_query='Orlat+Lwowskich+48+Warszawa'

                print(adres_query)
                if nr_lokalu.strip() != '':
                    adres = f"{ulica} {nr_domu}, {nr_lokalu}"
                else:
                    adres = f"{ulica} {nr_domu}"

                a = requests.get(f"https://nominatim.openstreetmap.org/search?q={adres_query}&format=geojson")
                if a.status_code == 200 and len(a.json()['features']) > 0:
                    szer = a.json()['features'][0]['geometry']['coordinates'][1]
                    dlug = a.json()['features'][0]['geometry']['coordinates'][0]
                else:
                    szer = 'n'
                    dlug = 'n'

                # write data to pandas dataframe
                df = df._append({'nazwa': nazwa, 'krs': krs, 'nip': nip, 'regon': regon, 'adres': adres, 'kod_pocztowy': kod_pocztowy, 'miejscowosc': miejscowosc, 'forma_prawna': forma_prawna, 'data_rejestracji': data_rejestracji, 'szer': szer, 'dlug': dlug}, ignore_index=True)
                
                
                # write to file
                f.write(f"{nazwa};{krs};{nip};{regon};{ulica} {nr_domu};{nr_lokalu};{kod_pocztowy};{miejscowosc};;{forma_prawna};{data_rejestracji};{szer};{dlug}\n")
            else:
                print('error')
                f.write(f"{krs};error\n")



# save pandas dataframe to csv file
df.to_csv('../pkgs/spoldzielnie/src/spoldzielnie/dane/spoldzielnie_df_5.csv', index=False)