from flask import render_template, url_for, request
from app import app
from .models import Personne, Lieu, Type, Image
from sqlalchemy import or_
from config import RESULTATS_PAR_PAGE, AUTRES_RESULTATS


# Pour les pages qui n'affichent que le contenu qu'elles ont, la route ne prend pas de paramètres
@app.route('/')
def accueil():
    return render_template('pages/accueil.html')


@app.route('/course_contre_la montre')
def course():
    return render_template('pages/course.html')


@app.route('/victimes')
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


@app.route('/recherche')
def recherche():
    return render_template('pages/recherche.html')


@app.route('/secours')
def secours():
    return render_template('pages/secours.html')


@app.route('/reconstruction')
def reconstruction():
    return render_template('pages/reconstruction.html')


@app.route('/generosite')
def generosite():
    return render_template('pages/generosite.html')


# Pour les fiches de personnes auxquelles on accède par la recherche, on donne comme paramètre l'id de la db Personne
# On sélectionne une personne et on injecte les infos de cette notice dans le template.
@app.route("/notice/<int:personne_id>")
def notice(personne_id):
    noticep = Personne.query.get(personne_id)
    return render_template("pages/personne.html", noticep=noticep)


# Pour les fiches de personnes auxquelles on accède par la recherche, on donne comme paramètre l'id de la db Lieu
# On sélectionne une personne et on injecte les infos de cette notice dans le template.
@app.route("/lieu/<int:lieu_id>")
def village(lieu_id):
    noticev = Lieu.query.get(lieu_id)
    return render_template("pages/village.html", noticev=noticev)


# On crée une page pour la map, qui ne comporte rien d'autre que la map.
@app.route('/map')
def carte():
    return render_template('pages/map.html')

# On définit quels sont les 4 types que le dropdown propose avec la variable type.
@app.route('/rechercheavancee')
def rechercheavancee():
    types = Type.query.order_by(Type.type_label).all()
    return render_template('pages/rechercheavancee.html', types=types)

# On fait la recherche du motclef donné par l'utilisateur dans la db Personne // VOIR POUR LIEU
@app.route('/resultats')
def search_results():

    motclef = request.args.get("motclef", None)
    page = request.args.get("page", 1, type=int)
    results = []
    places = []
    autres_results = []

    mots = motclef.split()

    for mot in mots:
        results = Personne.query.filter(or_(
            Personne.nom.like("%{}%".format(mot)),
            Personne.prenom.like("%{}%".format(mot)),
        )).order_by(Personne.nom.asc()).paginate(page=page, per_page=RESULTATS_PAR_PAGE)
        places = Lieu.query.filter(
            Lieu.nom.like("%{}%".format(mot))).order_by(Lieu.nom.asc()).paginate(
            page=page, per_page=RESULTATS_PAR_PAGE)
        autres_results = Personne.query.filter(or_(Personne.age.like("%{}%".format(mot)),
            Personne.travail.like("%{}%".format(mot)),
            Personne.fonction.like("%{}%".format(mot)),
            Personne.donnees_biographiques.like("%{}%".format(mot)),
            Personne.informations_complementaires.like("%{}%".format(mot)),
            Personne.levee_de_corps.like("%{}%".format(mot)),
            Personne.mission_debacle.like("%{}%".format(mot)),
        )).order_by(Personne.nom.asc()).paginate(page=page, per_page=AUTRES_RESULTATS)

    titre = "Recherche"


    return render_template("pages/resultat.html", results=results, autres_results=autres_results, places=places, titre=titre)


# La recherche peut être spécifiquement dans certains champs de la db
@app.route('/resultatavance')
def resultatavance():

    motclef = request.args.get("motclef", None)
    nom = request.args.get("nom", None)
    prenom = request.args.get("prenom", None)
    de = request.args.get("de", None)
    domicile = request.args.get("domicile", None)
    role = request.args.get("role", None)
    lieu = request.args.get("lieu", None)
    page = request.args.get("page", 1, type=int)

    resultats = []
    village = []


    if motclef:
        mots = motclef.split()

        for mot in mots:
            resultats = Personne.query.filter(or_(
                Personne.nom.like("%{}%".format(mot)),
                Personne.prenom.like("%{}%".format(mot)),
            )).order_by(Personne.nom.asc()).paginate(page=page, per_page=RESULTATS_PAR_PAGE)
            village = Lieu.query.filter(
                Lieu.nom.like("%{}%".format(mot))).order_by(Lieu.nom.asc()).paginate(
                page=page, per_page=RESULTATS_PAR_PAGE)
            autres_results = Personne.query.filter(or_(Personne.age.like("%{}%".format(mot)),
                                                       Personne.travail.like("%{}%".format(mot)),
                                                       Personne.fonction.like("%{}%".format(mot)),
                                                       Personne.donnees_biographiques.like("%{}%".format(mot)),
                                                       Personne.informations_complementaires.like("%{}%".format(mot)),
                                                       Personne.levee_de_corps.like("%{}%".format(mot)),
                                                       Personne.mission_debacle.like("%{}%".format(mot)),
                                                       )).order_by(Personne.nom.asc()).paginate(page=page,
                                                                                                per_page=AUTRES_RESULTATS)

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
            Personne.lieu_de_naissance.has(Lieu.nom == de)).order_by(Personne.nom.asc()).paginate(
            page=page, per_page=RESULTATS_PAR_PAGE)

    if domicile:
        resultats = Personne.query.filter(
            Personne.lieu_de_domicile.has(Lieu.nom== domicile)).order_by(Personne.nom.asc()).paginate(
            page=page, per_page=RESULTATS_PAR_PAGE)

    if role and role != "all":
        resultats = Personne.query.filter(
            Personne.type.has(Type.type_label == role)).order_by(Personne.nom.asc()).paginate(
            page=page, per_page=RESULTATS_PAR_PAGE)

    if lieu:
        village = Lieu.query.filter(
            Lieu.nom.like("%{}%".format(lieu))).order_by(Lieu.nom.asc()).paginate(
            page=page, per_page=RESULTATS_PAR_PAGE)

    titre = "Résultats"
    return render_template('pages/resultatavance.html', resultats=resultats, titre=titre, motclef=motclef, nom=nom,
                           prenom=prenom, de=de, domicile=domicile, role=role, lieu=lieu, village=village)

@app.route('/iiif/<url>')
def visionneuse(url):
    return render_template('pages/example.html')


@app.route('/index/personne')
def indexp():
    personne = Personne.query.order_by(Personne.nom.asc()).all()
    return render_template('pages/indexp.html', personne=personne)

@app.route('/index/lieu')
def indexl():
    lieu = Lieu.query.order_by(Lieu.nom.asc()).all()
    return render_template('pages/indexl.html', lieu=lieu)


