from flask import jsonify
from flask_restful import Resource, reqparse
from datetime import datetime
from app.models import TaskLink as DBTaskLink
from app import db


link_parser = reqparse.RequestParser()
link_parser.add_argument('source', type=int, help='link source')
link_parser.add_argument('target', type=int, help='link destination')
link_parser.add_argument('type', type=int, help='link type')


class Link(Resource):

    # create a new link between two tasks
    def post(self):
        args = link_parser.parse_args()
        temp_tasklink = DBTaskLink()
        temp_tasklink.source = args['source']
        temp_tasklink.target = args['target']
        temp_tasklink.type = args['type']
        db.session.add(temp_tasklink)
        db.session.commit()

        return jsonify(temp_tasklink.serialize)

    # Update a existing task
    def put(self,tasklink_id):
        args = task_parser.parse_args()

        temp_tasklink = DBTaskLink.query.get(tasklink_id)
        temp_tasklink.source = args['source']
        temp_tasklink.target = args['target']
        temp_tasklink.type = args['type']

        db.session.add(temp_task)
        db.session.commit()

        return jsonify(temp_task.serialize)

    # Delete a existing link
    def delete(self, tasklink_id):
        DBTaskLink.query.filter_by(id=tasklink_id).delete()
        db.session.commit()
        return
