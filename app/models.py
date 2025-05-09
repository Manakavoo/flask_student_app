# # Define SQLAlchemy models here
# from app import db

# class Application(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     academic_background = db.Column(db.Text, nullable=False)
#     status = db.Column(db.String(20), default='pending')

from app import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    academic_background = db.Column(db.Text, nullable=False)
    degree_certificate = db.Column(db.String(255), nullable=True)  # File path for the degree certificate
    id_proof = db.Column(db.String(255), nullable=True)  # File path for the ID proof
    status = db.Column(db.String(20), default='pending')

    def __repr__(self):
        return f"<Application {self.name}>"
    
    
