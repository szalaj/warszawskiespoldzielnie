from flask import Blueprint, render_template, flash, redirect, url_for, request, send_file, sessions, jsonify
import geojson
from ..models import Spoldzielnia, Sprawa
import csv
import pandas as pd
from os.path import join, dirname, realpath

STATIC_FOLDER = join(dirname(realpath(__file__)), '../static')
common = Blueprint('common', __name__)

@common.route('/favicon')
def favicon():
    return url_for('static', filename='favicon.ico')


@common.route('/', methods=['GET', 'POST'])
def main():

    # kr = Spoldzielnia.query.all()

    # S = [i.as_dict() for i in kr]
    # print(S)

    # UPLOADS_PATH = join(STATIC_FOLDER, 'spoldzielnie.csv')

    # # write S as csv
    # with open(UPLOADS_PATH ,'w') as f:
    #     writer = csv.DictWriter(f, fieldnames=S[0].keys())
    #     writer.writeheader()
    #     writer.writerows(S)




    return render_template('index.html')

@common.route('/spoldzielnie_dane', methods=['GET'])
def spoldzielnie_dane():
    S = Spoldzielnia.query.order_by(Spoldzielnia.nazwa).all()
    return jsonify([s.as_dict() for s in S])

@common.route('/sprawy_dane', methods=['GET'])
def sprawy_dane():
    S = Sprawa.query.order_by(Sprawa.spoldzielnia).all()
    return jsonify([s.as_dict() for s in S])