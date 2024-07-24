from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, nullable=False)


    def __repr__(self):
        return f'<Subject {self.subject}>'
    
    def to_json(self):
        return {
            "id":self.id,
            "subject":self.subject,
            "description":self.description,
            "completed":self.completed,
            "date":self.date
        }
