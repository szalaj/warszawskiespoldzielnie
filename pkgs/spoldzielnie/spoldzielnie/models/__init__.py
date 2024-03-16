
from .. import db
from sqlalchemy.sql import func

class Spoldzielnia(db.Model):
    __tablename__ = 'spoldzielnia'


    krs  = db.Column(db.String, primary_key=True) 
    nazwa = db.Column(db.String) 

    nip = db.Column(db.String) 
    regon = db.Column(db.String) 
    adres = db.Column(db.String) 
    kod_pocztowy = db.Column(db.String)
    miejscowosc = db.Column(db.String)
    forma_prawna = db.Column(db.String) 
    data_rejestracji = db.Column(db.DateTime())
    status = db.Column(db.String)
    szerokosc_geo = db.Column(db.String)
    dlugosc_geo = db.Column(db.String)



    def __repr__(self):
        return f"{self.nazwa} - {self.krs} - {self.kod_pocztowy}"
    
    def as_dict(self):
        return {'nazwa': self.nazwa, 'szerokosc_geo': self.szerokosc_geo, 'dlugosc_geo': self.dlugosc_geo, 'krs': self.krs, 'nip': self.nip, 'regon': self.regon, 'adres': self.adres, 'kod_pocztowy': self.kod_pocztowy, 'miejscowosc': self.miejscowosc, 'forma_prawna': self.forma_prawna, 'data_rejestracji': self.data_rejestracji, 'status': self.status}
    
