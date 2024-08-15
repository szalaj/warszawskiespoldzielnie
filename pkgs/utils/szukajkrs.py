import re


with open('../pkgs/spoldzielnie/spoldzielnie/dane/rejestrio_spol_wawa', 'r') as f:
    data = f.read()

    # search regex patter in data and return list of matches
    # patter KRS.*

    krs = re.findall(r'KRS.*', data)
    for i in krs:
        print(i.split(' ')[1])



# https://api-krs.ms.gov.pl/api/krs/OdpisAktualny/0000010235?rejestr=P&format=json