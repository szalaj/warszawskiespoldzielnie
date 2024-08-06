
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
    dzielnica = db.Column(db.String)
    forma_prawna = db.Column(db.String) 
    data_rejestracji = db.Column(db.DateTime())
    status = db.Column(db.String)
    szerokosc_geo = db.Column(db.String)
    dlugosc_geo = db.Column(db.String)

    
    def as_dict(self):
        return {'nazwa': self.nazwa, 'szerokosc_geo': self.szerokosc_geo, 'dlugosc_geo': self.dlugosc_geo, 'krs': self.krs, 'nip': self.nip, 'regon': self.regon, 'adres': self.adres, 'kod_pocztowy': self.kod_pocztowy, 'miejscowosc': self.miejscowosc, 'dzielnica': self.dzielnica, 'forma_prawna': self.forma_prawna, 'data_rejestracji': self.data_rejestracji, 'status': self.status}
    

class Sprawa(db.Model):
    __tablename__ = 'sprawa'

    nr = db.Column(db.Integer, primary_key=True) 
    data_dodania = db.Column(db.DateTime(timezone=True), server_default=func.now())

    spoldzielnia = db.Column(db.String, db.ForeignKey("spoldzielnia.krs"), nullable=False)

    zgloszenie = db.Column(db.String)
    kontakt = db.Column(db.String)

    data_rozpoczenia = db.Column(db.DateTime())
    data_zakonczenia = db.Column(db.DateTime())

    opis = db.Column(db.String)
    status = db.Column(db.String)
    rozwiazanie = db.Column(db.String)
    temat = db.Column(db.String)
    typ = db.Column(db.String)

    odnosniki = db.Column(db.String)
    uwagi = db.Column(db.String)

    szerokosc_geo = db.Column(db.String)
    dlugosc_geo = db.Column(db.String)



    def __repr__(self):
        return f"{self.spoldzielnia} - {self.opis}"
    
    def as_dict(self):
        return {'nr': self.nr, 'spoldzielnia': self.spoldzielnia, 'data_rozpoczenia': self.data_rozpoczenia, 'data_zakonczenia': self.data_zakonczenia, 'opis': self.opis, 'status': self.status, 'typ':self.typ, 'temat': self.temat, 'odnosniki': self.odnosniki, 'szerokosc_geo': self.szerokosc_geo, 'dlugosc_geo': self.dlugosc_geo}
    

class Walne(db.Model):
    __tablename__ = 'walne'


    nr = db.Column(db.Integer, primary_key=True) 

    data_dodania = db.Column(db.DateTime(timezone=True), server_default=func.now())

    spoldzielnia = db.Column(db.String, db.ForeignKey("spoldzielnia.krs"), nullable=False)

    rok = db.Column(db.Integer)

    uchwala_zatw = db.Column(db.Boolean)


    kiedy_bylo = db.Column(db.DateTime())



    bilans = db.Column(db.Float)

    uwagi = db.Column(db.String)



    def __repr__(self):
        return f"{self.spoldzielnia} - {self.bilans}"
    
    def as_dict(self):
        return {'nr': self.nr, 'spoldzielnia': self.spoldzielnia, 'uchwala_zatw': self.uchwala_zatw, 'kiedy_bylo': self.kiedy_bylo, 'bilans': self.bilans, 'uwagi': self.uwagi}

class Organizacja(db.Model):
    __tablename__ = 'organizacja'


    nr = db.Column(db.Integer, primary_key=True) 
    data_dodania = db.Column(db.DateTime(timezone=True), server_default=func.now())

    spoldzielnia = db.Column(db.String, db.ForeignKey("spoldzielnia.krs"), nullable=False)



    data_powstania = db.Column(db.DateTime())
    data_koniec = db.Column(db.DateTime())

    nazwa = db.Column(db.String)
    status = db.Column(db.String)
    dzialalnosc = db.Column(db.String)
    opis = db.Column(db.String)
    miejscowosc = db.Column(db.String)

    odnosniki = db.Column(db.String)
    uwagi = db.Column(db.String)

    szerokosc_geo = db.Column(db.String)
    dlugosc_geo = db.Column(db.String)



    def __repr__(self):
        return f"{self.spoldzielnia} - {self.opis}"
    
    def as_dict(self):
        return {'nr': self.nr, 'spoldzielnia': self.spoldzielnia, 'data_powstania': self.data_powstania, 'data_koniec': self.data_koniec, 'nazwa': self.nazwa, 'status': self.status, 'dzialalnosc': self.dzialalnosc, 'opis': self.opis, 'miejscowosc': self.miejscowosc, 'odnosniki': self.odnosniki, 'uwagi': self.uwagi, 'szerokosc_geo': self.szerokosc_geo, 'dlugosc_geo': self.dlugosc_geo}