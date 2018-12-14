from datetime import timedelta

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, marshal_with, reqparse, abort

from src.messages.messages import COMMUNIY_DOESNT_EXIST, UNAUTHORIZED, TASK_MUST_BE_EITHER_TIME_OR_KM_TRIGGERED, \
    INTERNAL_SERVER_ERROR
from src.models.community import CommunityModel
from src.models.task import TaskModel
from src.models.user import UserModel
from src.util.parser_types import moment


class CreateTask(Resource):

    @jwt_required
    @marshal_with(TaskModel.get_marshaller())
    def post(self, community_id):
        parser = reqparse.RequestParser()
        parser.add_argument('time_interval_start', type=moment, required=False)
        parser.add_argument('time_interval', type=int, required=False)
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('km_interval', type=int, required=False)
        parser.add_argument('km_interval_start', type=float, required=False)
        data = parser.parse_args()

        owner = UserModel.find_by_username(get_jwt_identity())
        community: CommunityModel = CommunityModel.find_by_id(community_id)
        community_member_ids = [m.id for m in community.users]

        if not community:
            abort(400, message=COMMUNIY_DOESNT_EXIST)

        if owner.id not in community_member_ids:
            abort(401, message=UNAUTHORIZED)

        if not (data['time_interval_start'] and data['time_interval'] or data['km_interval'] and data[
            'km_interval_start']) or data['km_interval'] and (data['time_interval'] or data['time_interval_start']) or \
                data['time_interval'] and (data['km_interval'] or data['km_interval_start']):
            abort(400, message=TASK_MUST_BE_EITHER_TIME_OR_KM_TRIGGERED)

        time_interval_start = None
        if data['time_interval_start']:
            time_interval_start = timedelta(days=data['time_interval'])

        new_task = TaskModel(
            owner=owner,
            community=community,
            time_interval=time_interval_start,
            time_interval_start=data['time_interval_start'],
            km_interval=data['km_interval'],
            km_interval_start=data['km_interval_start'],
            name=data['name'],
            description=data['description'],
        )

        try:
            new_task.persist()
            return new_task, 201
        except:
            abort(500, message=INTERNAL_SERVER_ERROR)
