from app import db


class Lieu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.TEXT, index=True, unique=True)
    commune = db.Column(db.TEXT, index=True, unique=True)
    personnes = db.relationship('Personne', backref='origine', lazy='dynamic')

    def __repr__(self):
        return '<Lieu {}>'.format(self.username)


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.TEXT, index=True, unique=True)
    personne = db.relationship('Personne', backref='genre', lazy='dynamic')

    def __repr__(self):
        return '<Type {}>'.format(self.username)


class Personne(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.TEXT, index=True)
    prenom = db.Column(db.TEXT, index=True)
    age = db.Column(db.Integer, index=True)
    de = db.Column (db.Integer, db.ForeignKey("lieu.id"))
    domicile = db.Column (db.Integer, db.ForeignKey("lieu.id"))
    travail = db.Column(db.TEXT)
    type = db.Column (db.Integer, db.ForeignKey("type.id"))
    fonction = db.Column(db.TEXT)
    donnees_biographiques = db.Column(db.TEXT)
    levee_de_corps = db.Column(db.TEXT)
    informations_complementaires = db.Column(db.TEXT)
    mission_debacle = db.Column(db.TEXT)
    correspondance = db.Column(db.TEXT)

    def __repr__(self):
        return '<Personne {}>'.format(self.username)


    def __repr__(self):
        return '<User {}>'.format(self.username)