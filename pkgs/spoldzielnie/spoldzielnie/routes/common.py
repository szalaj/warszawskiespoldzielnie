from flask import Blueprint, render_template, flash, redirect, url_for, request, send_file, sessions
import geojson
common = Blueprint('common', __name__)

@common.route('/', methods=['GET', 'POST'])
def main():

    # with open('static/dzielnice/warszawa-dzielnice.geojson', 'r') as F:
    #     city_districts = geojson.loads(F.read())    

    return render_template('index.html')