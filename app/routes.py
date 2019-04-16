from flask import render_template, url_for, request
from app import app
from .models import Personne, Lieu, Type
from sqlalchemy import or_
from config import RESULTATS_PAR_PAGE


@app.route('/')
def accueil():
    return render_template('pages/accueil.html')


@app.route('/course contre la montre')
def course():
    return render_template('pages/course.html')


@app.route('/victime')
def victime():
    resultats = Personne.query.all()
    return render_template('pages/victime.html', resultats=resultats)


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


@app.route('/resultats')
def search_results():
    motclef = request.args.get("keyword", None)

    page = request.args.get("page", 1)
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    results = []
    titre = "Recherche"
    if motclef:
        results = Personne.query.filter(or_(
            Personne.nom.like("%{}%".format(motclef)),
            Personne.prenom.like("%{}%".format(motclef)),
            Personne.age.like("%{}%".format(motclef)),
            Personne.travail.like("%{}%".format(motclef)),
            Personne.fonction.like("%{}%".format(motclef)),
            Personne.donnees_biographiques.like("%{}%".format(motclef)),
            Personne.informations_complementaires.like("%{}%".format(motclef)),
            Personne.levee_de_corps.like("%{}%".format(motclef)),
            Personne.mission_debacle.like("%{}%".format(motclef)),
        )).order_by(Personne.nom.asc()).paginate(page=page, per_page=RESULTATS_PAR_PAGE)
        titre = "Résultat pour la recherche '" + motclef + "'"

    return render_template(
        "pages/resultat.html",
        results=results,
        titre=titre,
        keyword=motclef)


@app.route("/notice/<int:personne_id>")
def notice(personne_id):
    noticep = Personne.query.get(personne_id)
    return render_template("pages/personne.html", noticep=noticep)


@app.route('/map')
def carte():
    return render_template('pages/map.html')


@app.route('/rechercheavancee')
def rechercheavancee():
    types = Type.query.order_by(Type.type_label).all()
    return render_template('pages/rechercheavancee.html', types=types)


@app.route('/resultatavance')
def resultatavance():
    # on récupère les valeurs de recherche
    motclef = request.args.get("motclef", None)
    nom = request.args.get("nom", None)
    prenom = request.args.get("prenom", None)
    de = request.args.get("de", None)
    domicile = request.args.get("domicile", None)
    role = request.args.get("role", None)

    page = request.args.get("page", 1)
    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    resultats = []

    if motclef:
        resultats = Personne.query.filter(or_(
            Personne.nom.like("%{}%".format(motclef)),
            Personne.prenom.like("%{}%".format(motclef)),
            Personne.age.like("%{}%".format(motclef)),
            Personne.travail.like("%{}%".format(motclef)),
            Personne.fonction.like("%{}%".format(motclef)),
            Personne.donnees_biographiques.like("%{}%".format(motclef)),
            Personne.informations_complementaires.like("%{}%".format(motclef)),
            Personne.levee_de_corps.like("%{}%".format(motclef)),
            Personne.mission_debacle.like("%{}%".format(motclef)),
        )).order_by(Personne.nom.asc()).paginate(page=page, per_page=RESULTATS_PAR_PAGE)

    if nom:
        resultats = Personne.query.filter(
            Personne.nom.like("%{}%".format(nom))).order_by(Personne.nom.asc()).paginate(
            page=page, per_page=RESULTATS_PAR_PAGE)

    if prenom:
        resultats = Personne.query.filter(
            Personne.prenom.like("%{}%".format(prenom))).order_by(Personne.nom.asc()).paginate(
            page=page, per_page=RESULTATS_PAR_PAGE)

    if de:
        resultats = Personne.query.filter(
            Personne.de.like("%{}%".format(de))).order_by(Personne.nom.asc()).paginate(
            page=page, per_page=RESULTATS_PAR_PAGE)

    if domicile:
        resultats = Personne.query.filter(
            Personne.domicile.like("%{}%".format(domicile))).order_by(Personne.nom.asc()).paginate(
            page=page, per_page=RESULTATS_PAR_PAGE)

    if role and role != "all":
        resultats = Personne.query.filter(
            Personne.type_id.any(Type.type_label == role)).order_by(Personne.nom.asc()).paginate(
            page=page, per_page=RESULTATS_PAR_PAGE)

    titre = "Résultats"
    return render_template('pages/resultatavance.html', resultats=resultats, titre=titre, motclef=motclef, nom=nom,
                           prenom=prenom, de=de, domicile=domicile, role=role)