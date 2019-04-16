from app import db


class Lieu(db.Model):
    __tablename__ = "lieu"
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.TEXT, index=True, unique=True)
    commune = db.Column(db.TEXT, index=True, unique=True)


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
    domicile = db.Column(db.Integer, db.ForeignKey("lieu.id"))
    de = db.Column(db.Integer, db.ForeignKey("lieu.id"))
    travail = db.Column(db.TEXT)
    type_id = db.Column(db.Integer, db.ForeignKey("type.typeId"))
    fonction = db.Column(db.TEXT)
    donnees_biographiques = db.Column(db.TEXT)
    levee_de_corps = db.Column(db.TEXT)
    informations_complementaires = db.Column(db.TEXT)
    mission_debacle = db.Column(db.TEXT)
    correspondance = db.Column(db.TEXT)
    wikipedia = db.Column(db.TEXT)
    dhs = db.Column(db.TEXT)
    type = db.relationship("Type")
