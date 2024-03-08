from flask import Blueprint, render_template, flash, redirect, url_for, request, send_file, sessions
common = Blueprint('common', __name__)

@common.route('/', methods=['GET', 'POST'])
def main():


    return render_template('index.html')