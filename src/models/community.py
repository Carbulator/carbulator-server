from flask_restful import fields

from src.app import db
from src.exceptions.no_data import NoData
from src.models.car import CarModel
from src.models.user import UserModel


class CommunityModel(db.Model):
    __tablename__ = 'communities'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    users = db.relationship('UserModel', secondary='community_user_link',
                            secondaryjoin='and_(CommunityUserLinkModel.user_id == UserModel.id, '
                                          'CommunityUserLinkModel.invitation_accepted == True)')
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), unique=True)
    car = db.relationship("CarModel", backref=db.backref("community", uselist=False))

    def persist(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_marshaller():
        return {
            'id': fields.Integer,
            'name': fields.String,
            'time_created': fields.DateTime,
            'time_updated': fields.DateTime,
            'users': fields.List(fields.Nested(UserModel.get_marshaller())),
            'car': fields.Nested(CarModel.get_marshaller())
        }

    @staticmethod
    def get_detailed_marshaller():
        return {
            'id': fields.Integer,
            'name': fields.String,
            'time_created': fields.DateTime,
            'time_updated': fields.DateTime,
            'users': fields.List(fields.Nested(UserModel.get_marshaller())),
            'car': fields.Nested(CarModel.get_marshaller()),
            'is_deletable': fields.Boolean,
            'is_editable': fields.Boolean
        }

    @classmethod
    def find_by_car_id(cls, id):
        return cls.query.filter_by(car_id=id).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def return_all(cls):
        return CommunityModel.query.all()

    @classmethod
    def delete_all(cls):
        db.session.query(cls).delete()
        db.session.commit()

    @classmethod
    def delete_by_id(cls, id):
        community = db.session.query(cls).filter(cls.id == id).first()
        if community:
            db.session.delete(community)
            db.session.commit()
        else:
            raise NoData
