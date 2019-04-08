from flask import render_template, url_for
from werkzeug.urls import url_parse
from app import app


@app.route('/')
def accueil():
    return render_template('pages/accueil.html')


@app.route('/course contre la montre')
def course():
    return render_template('pages/course.html')


@app.route('/victime')
def victime():
    return render_template('pages/victime.html')


@app.route('/bienfaisance')
def bienfaisance():
    return render_template('pages/bienfaisance.html')


@app.route('/ombre')
def ombre():
    return render_template('pages/ombre.html')


@app.route('/souvenir')
def souvenir():
    return render_template('pages/souvenir.html')


@app.route('/approfondir')
def approfondir():
    return render_template('pages/pourapp.html')


@app.route('/recherche')
def recherche():
    return render_template('pages/recherche.html')

@app.route('/secours')
def secours():
    return render_template('pages/secours.html')