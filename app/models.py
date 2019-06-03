from app import db
from flask import url_for


class Lieu(db.Model):
    __tablename__ = "lieu"
    lieuId = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.TEXT, index=True, unique=True)
    commune = db.Column(db.TEXT, index=True, unique=True)
    degats = db.Column(db.TEXT)
    nombre_morts= db.Column(db.TEXT)
    animaux_emportes = db.Column(db.TEXT)


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


class Document(db.Model):
    __tablename__ = "image"
    image_id = db.Column(db.Integer, primary_key=True)
    image_cote = db.Column(db.TEXT)
    type = db.Column(db.TEXT)
    emetteur = db.Column(db.TEXT)
    destinataire = db.Column(db.TEXT)
    date = db.Column(db.TEXT)
    lieu = db.Column(db.TEXT)  # missed opportunity? A réfléchir.
    sujet = db.Column(db.TEXT)

    def to_dict(self):
        data = {
            'image_id': self.image_id,
            "image_cote": self.image_cote,
            "type": self.type,
            "emetteur": self.emetteur,
            "destinataire": self. destinataire,
            "date": self.date,
            "lieu": self.lieu,
            "sujet": self.sujet,
            "_links": {"self": url_for ("api.get_document", id=self.id)}
            }
        return data


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data

