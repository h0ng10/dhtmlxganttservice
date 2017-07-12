import click
import os
from datetime import datetime
from flask import Flask
from app import create_app, db, models

app = create_app((os.getenv('FLASK_CONFIG') or 'default'))

@app.cli.command()
#@click.option('--coverage/--no-coverage', default=False, help='Enable code coverage')
def initdb():
    """Initialize the database."""
    db.create_all()


@app.cli.command()
#@click.option('--coverage/--no-coverage', default=False, help='Enable code coverage')
def cleardb():
    """Clear the database."""
    db.drop_all()


@app.cli.command()
def addtestdata():
    """Add some test data to the database"""

    task1 = models.Task()
    task1.text = "Testtask1"
    task1.start_date = datetime.strptime("2017-09-01", "%Y-%m-%d")
    task1.duration = 5
    task1.progress = 0.8
    task1.sortorder = 20
    task1.parent = 0

    db.session.add(task1)
    db.session.commit()
