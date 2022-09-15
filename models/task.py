from db import db

class TaskModel(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    descrip = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self, id, descrip, status):
        self.id = id
        self.descrip = descrip
        self.status = status

    def json(self, depth =0):
        json = {
            'id': self.id,
            'descrip': self.descrip,
            'status': self.status
        }

        return json
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()