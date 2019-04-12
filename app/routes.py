from flask import render_template, url_for, request
from app import app
from .models import Personne, Lieu, Type
from sqlalchemy import or_

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
        )).order_by(Personne.nom.asc()).paginate()
        titre = "Résultat pour la recherche '" + motclef + "'"

    return render_template(
        "pages/resultat.html",
        results=results,
        titre=titre,
        keyword=motclef)

@app.route("/notice/<int:personne_id>")
def notice(personne_id):
    noticep= Personne.query.get(personne_id)
    return render_template("pages/personne.html", noticep=noticep)


