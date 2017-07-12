from flask import jsonify
from flask_restful import Resource, reqparse
from datetime import datetime
from app.models import Task as DBTask
from app.models import TaskLink as DBTaskLink
from app import db


task_parser = reqparse.RequestParser()
task_parser.add_argument('text', type=str, help='A short description of the task')
task_parser.add_argument('parent', type=int, help='ID of the parent task (or 0)')
task_parser.add_argument('duration', type=int, help='The task duration (in days)')
task_parser.add_argument('progress', type=float, help='Progress of the task')
task_parser.add_argument('start_date', type=lambda x: datetime.strptime(x,'%d-%m-%Y %H:%M'), help='Start date of the task')
task_parser.add_argument('end_date', type=lambda x: datetime.strptime(x,'%d-%m-%Y %H:%M'), help='End date of the task')


class Task(Resource):

    # create a new task
    def post(self):
        args = task_parser.parse_args()

        temp_task = DBTask()
        temp_task.text = args['text']
        temp_task.parent = args['parent']
        temp_task.duration = args['duration']
        temp_task.start_date = args['start_date']
        temp_task.progress = 0
        temp_task.sortorder = 0

        db.session.add(temp_task)
        db.session.commit()

        return jsonify(temp_task.serialize)

    # Update a existing task
    def put(self,task_id):
        args = task_parser.parse_args()

        temp_task = DBTask.query.get(task_id)
        temp_task.text = args['text']
        temp_task.parent = args['parent']
        temp_task.duration = args['duration']
        temp_task.start_date = args['start_date']
        temp_task.progress = args['progress']
        temp_task.sortorder = 0

        db.session.add(temp_task)
        db.session.commit()

        return jsonify(temp_task.serialize)

    # Delete a existing task
    def delete(self, task_id):
        DBTask.query.filter_by(id=task_id).delete()
        db.session.commit()
        return


class TaskList(Resource):
    def get(self):
        tasks = DBTask.query.all()
        links = DBTaskLink.query.all()
        return jsonify(data=[i.serialize for i in tasks],links=[j.serialize for j in links])
