from app import db


class Lieu(db.Model):
    __tablename__ = "lieu"
    lieuId = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.TEXT, index=True, unique=True)
    commune = db.Column(db.TEXT, index=True, unique=True)
    degats = db.Column(db.TEXT)
    nombre_morts= db.Column(db.TEXT)
    animaux_emportes = db.Column(db.TEXT)
    pertinent = db.Column(db.Integer)
    coordonnees = db.Column(db.Integer)


class Type(db.Model):
    __tablename__ = "type"
    typeId = db.Column(db.Integer, primary_key=True)
    type_label = db.Column(db.TEXT, index=True, unique=True)


class Personne(db.Model):
    __tablename__ = "personne"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.TEXT, index=True)
    prenom = db.Column(db.TEXT, index=True)
    age = db.Column(db.Integer, index=True)
    travail = db.Column(db.TEXT)
    type_id = db.Column(db.Integer, db.ForeignKey("type.typeId"))
    de = db.Column(db.Integer, db.ForeignKey("lieu.lieuId"))
    domicile = db.Column(db.Integer, db.ForeignKey("lieu.lieuId"))
    fonction = db.Column(db.TEXT)
    donnees_biographiques = db.Column(db.TEXT)
    levee_de_corps = db.Column(db.TEXT)
    informations_complementaires = db.Column(db.TEXT)
    mission_debacle = db.Column(db.TEXT)
    correspondance = db.Column(db.TEXT)
    wikipedia = db.Column(db.TEXT)
    dhs = db.Column(db.TEXT)
    type = db.relationship("Type")
    lieu_de_naissance = db.relationship("Lieu", foreign_keys=de)
    lieu_de_domicile = db.relationship("Lieu", foreign_keys=domicile)
    image = db.Column(db.TEXT)
    legende = db.Column(db.TEXT)
    document1 = db.Column(db.TEXT)
    document1url = db.Column(db.TEXT)
    document2 = db.Column(db.TEXT)
    document2url = db.Column(db.TEXT)
    document3 = db.Column(db.TEXT)
    document3url = db.Column(db.TEXT)
    document4 = db.Column(db.TEXT)
    document4url = db.Column(db.TEXT)
    document5 = db.Column(db.TEXT)
    document5url = db.Column(db.TEXT)
    document6 = db.Column(db.TEXT)
    document6url = db.Column(db.TEXT)
    document7 = db.Column(db.TEXT)
    document7url = db.Column(db.TEXT)
    document8 = db.Column(db.TEXT)
    document8url = db.Column(db.TEXT)
    document9 = db.Column(db.TEXT)
    document9url = db.Column(db.TEXT)
    document10 = db.Column(db.TEXT)
    document10url = db.Column(db.TEXT)
    document11 = db.Column(db.TEXT)
    document11url = db.Column(db.TEXT)
    source = db.Column(db.TEXT)
    lettre = db.Column(db.TEXT)


class Image(db.Model):
    __tablename__ = "image"
    image_id = db.Column(db.Integer, primary_key=True)
    image_cote = db.Column(db.TEXT)
    image_type = db.Column(db.TEXT)
    emetteur = db.Column(db.TEXT)
    destinataire = db.Column(db.TEXT)
    date = db.Column(db.TEXT)
    image_lieu = db.Column(db.TEXT)
    sujet = db.Column(db.TEXT)
    url = db.Column(db.TEXT)
