from flask import jsonify, render_template
from ..models import Task

from . import gantt

@gantt.route('/')
def index():
    return render_template('ganttchart.html')

@gantt.route('/ganttest2')
def ganttest2():
    tasks = Task.query.all()
    return jsonify(data=[i.serialize for i in tasks])
