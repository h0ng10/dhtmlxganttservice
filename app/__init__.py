from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	# config[config_name].init_app(app)

	db.init_app(app)

	# attach routes and custom error pages here
	from .gantt import gantt as gantt_blueprint
	app.register_blueprint(gantt_blueprint)

	from .api_1_0 import restapi_blueprint
	app.register_blueprint(restapi_blueprint, url_prefix='/api/v1.0')


	return app
