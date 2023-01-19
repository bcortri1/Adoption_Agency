from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connects to database."""
    db.app = app
    db.init_app(app)
    
    
class Pet(db.Model):
    """Contains all information related to a pet"""
    def __repr__(self):
        return f"Pet: {self.id} {self.name} {self.species} {self.age} {self.available}"
    
    __tablename__ = "adopt"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    species = db.Column(db.String(25), nullable=False)
    photo_url = db.Column(db.String(150), nullable=False, default = "http://www.clker.com/cliparts/M/P/w/l/3/v/question-mark-md.png")
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(50), nullable=True)
    available = db.Column(db.Boolean, nullable=False, default = True)