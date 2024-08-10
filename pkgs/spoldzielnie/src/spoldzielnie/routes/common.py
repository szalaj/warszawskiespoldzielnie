from flask import Blueprint, render_template, flash, redirect, url_for, request, send_file, sessions, jsonify
import geojson
from spoldzielnie.models import Spoldzielnia, Sprawa, Walne
import csv
import pandas as pd
from os.path import join, dirname, realpath
from spoldzielnie import db
from datetime import datetime
from loguru import logger

STATIC_FOLDER = join(dirname(realpath(__file__)), '../static')
common = Blueprint('common', __name__)

@common.route('/favicon')
def favicon():
    return url_for('static', filename='favicon.ico')


@common.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')


@common.route('/spoldzielnie', methods=['GET'])
def spoldzielnie():

    return render_template('spoldzielnia.html')

@common.route('/artykuly', methods=['GET'])
def artykuly():
    return render_template('artykuly.html')

@common.route('/artykuly_dane', methods=['GET'])
def artykuly_dane():

    result = db.session.query(Sprawa, Spoldzielnia).join(
        Spoldzielnia, Spoldzielnia.krs == Sprawa.spoldzielnia, 
        isouter=True).all()
    

    S=[]
    for spr, s in result:

        S.append({
            'krs': s.krs if s else 'None',
            'nazwa': s.nazwa if s else '',
            'miejscowosc': s.miejscowosc if s else '',
            'data_rozpoczenia': spr.data_rozpoczenia,
            'temat': spr.temat,
            'typ': spr.typ,
            'opis': spr.opis,
            'status': spr.status,
            'rozwiazanie': spr.rozwiazanie,
            'odnosniki': spr.odnosniki


        }
            
        )

    return jsonify([s for s in S])


@common.route('/spoldzielnie_dane', methods=['GET'])
def spoldzielnie_dane():

    # query dane from Spoldzielnia and join bilans data from Walne by krs, show all columns

    #S = Spoldzielnia.query.join(Walne, Spoldzielnia.krs == Walne.spoldzielnia).all()
    result = db.session.query(Spoldzielnia, Walne).join(
        Walne, Walne.spoldzielnia == Spoldzielnia.krs, 
        isouter=True).all()

    
    S=[]
    for s, w in result:

        if w.rok == 2022:

            S.append({
                'krs': s.krs,
                'bilans': w.bilans if w else 'do sprawdzenia',
                'nazwa': s.nazwa,
                'szerokosc_geo': s.szerokosc_geo,
                'dlugosc_geo': s.dlugosc_geo,
                'kod_pocztowy': s.kod_pocztowy,
                'miejscowosc': s.miejscowosc,
                'dzielnica': s.dzielnica,
                'forma_prawna': s.forma_prawna,
                'data_rejestracji': s.data_rejestracji,
                'status': s.status,
                'nip': s.nip,
                'regon': s.regon,
                'adres': s.adres,

            }
                
            )


    #S = Spoldzielnia.query.order_by(Spoldzielnia.nazwa).all()
    return jsonify([s for s in S])

@common.route('/sprawy_dane', methods=['GET'])
def sprawy_dane():
    S = Sprawa.query.order_by(Sprawa.spoldzielnia).all()
    return jsonify([s.as_dict() for s in S])

@common.route('/walne_dane', methods=['GET'])
def walne_dane():
    S = Sprawa.query.order_by(Walne.spoldzielnia).all()
    return jsonify([s.as_dict() for s in S])





