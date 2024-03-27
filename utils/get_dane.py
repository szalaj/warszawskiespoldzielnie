import requests

# create new csv file to write later


with open('../pkgs/spoldzielnie/spoldzielnie/dane/spoldzielnie_krs.txt', 'r') as f:
    data = f.read()
    # get first line

# create and open new csv file to write
with open('../pkgs/spoldzielnie/spoldzielnie/dane/spoldzielnie_krs_dane.csv', 'w') as f:
    for i,krs in enumerate(data.split('\n')):
        if i !=0:
            print(krs)
            rejestr = 'P'
            x = requests.get(f"https://api-krs.ms.gov.pl/api/krs/OdpisAktualny/{krs}?rejestr={rejestr}&format=json")
            print(x.status_code)
            if x.status_code == 200:
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

                
                # write to file
                f.write(f"{nazwa};{krs};{nip};{regon};{ulica} {nr_domu};{nr_lokalu};{kod_pocztowy};{miejscowosc};;{forma_prawna};{data_rejestracji}\n")
            else:
                print('error')
                f.write(f"{krs};error\n")