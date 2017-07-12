from app import db

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    progress = db.Column(db.Float, nullable=False)
    sortorder = db.Column(db.Integer, nullable=False)
    parent = db.Column(db.Integer, nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.id,
           'text'       : self.text,
           'start_date' : self.start_date.strftime("%d-%m-%Y"),
           'duration'   : self.duration,
           'progress'   : self.progress,
           'sortorder'  : self.sortorder,
           'parent'     : self.parent
       }


class TaskLink(db.Model):

    __tablename__ = "tasklinks"

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.Integer, nullable=False)
    target = db.Column(db.Integer,nullable=False)
    type = db.Column(db.String)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.id,
           'source'     : self.source,
           'target'     : self.target,
           'type'       : self.type
       }
