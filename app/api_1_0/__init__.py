from flask import Blueprint
from flask_restful import Api

from .resources.task import Task
from .resources.task import TaskList
from .resources.link import Link

restapi_blueprint = Blueprint('api', __name__)
restapi = Api(restapi_blueprint)

restapi.add_resource(TaskList, '/')
restapi.add_resource(Task, '/task', '/task/<int:task_id>')
restapi.add_resource(Link, '/link', '/link/<int:tasklink_id>')
