import datetime

from flask_restful import fields

from src.app import db
from src.exceptions.no_data import NoData
from src.messages.marshalling_custom_fields import TimedeltaDays
from src.models.community import CommunityModel
from src.models.user import UserModel


class TaskModel(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    time_updated = db.Column(db.DateTime(), onupdate=datetime.datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    owner = db.relationship('UserModel', foreign_keys=[owner_id])
    community_id = db.Column(db.Integer, db.ForeignKey('communities.id'), nullable=False)
    community = db.relationship('CommunityModel')
    km_interval = db.Column(db.Integer, nullable=True)
    km_next_instance = db.Column(db.DECIMAL(precision=10, scale=1), nullable=True)
    time_interval = db.Column(db.Interval, nullable=True)
    time_next_instance = db.Column(db.DateTime(), nullable=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(120))
    instances = db.relationship("TaskInstanceModel", cascade="all, delete")
    is_reocurrent = db.Column(db.Boolean, nullable=False, default=True)

    def persist(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_marshaller():
        return {
            'id': fields.Integer,
            'time_created': fields.DateTime,
            'time_updated': fields.DateTime,
            'time_next_instance': fields.DateTime,
            'time_interval': TimedeltaDays,
            'owner': fields.Nested(UserModel.get_marshaller()),
            'community': fields.Nested(CommunityModel.get_marshaller()),
            'name': fields.String,
            'description': fields.String,
            'km_interval': fields.Integer,
            'km_next_instance': fields.Float,
            'km_to_next_instance': fields.Float,
            'is_reocurrent': fields.Boolean
        }

    @classmethod
    def delete_by_id(cls, task_id):
        task = db.session.query(cls).filter(cls.id == task_id).first()
        if task:
            db.session.delete(task)
            db.session.commit()
        else:
            raise NoData

    @classmethod
    def find_by_id(cls, task_id):
        return cls.query \
            .filter_by(id=task_id) \
            .first()

    @classmethod
    def return_all(cls):
        return cls.query \
            .filter_by(is_reocurrent=True) \
            .all()

    @classmethod
    def find_by_community(cls, community_id):
        return cls.query \
            .filter_by(community_id=community_id) \
            .filter_by(is_reocurrent=True) \
            .all()
