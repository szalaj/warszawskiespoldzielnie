from flask_login import UserMixin
from .. import db
from sqlalchemy.sql import func

class Spoldzielnia(db.Model):
    __tablename__ = 'spoldzielnia'

    id = db.Column(db.Integer, primary_key=True)

    nazwa = db.Column(db.String) 
    krs  = db.Column(db.String) 
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
        return {'nazwa': self.nazwa, 'x': self.krs}
    
