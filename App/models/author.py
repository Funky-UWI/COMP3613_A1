from App.database import db
from werkzeug.security import check_password_hash, generate_password_hash

class Author(db.Model):
    __tablename__ = "author"
    id = db.Column("id", db.Integer, primary_key=True)
    first_name =  db.Column("first_name", db.String(60), nullable=False)
    last_name =  db.Column("last_name", db.String(60), nullable=False)
    email = db.Column("email", db.String(60), nullable=False)
    password = db.Column("password", db.String(60), nullable=False)
    # qualifications = db.Column("qualifications", db.ARRAY(db.String(120)), nullable=True)
    records = db.relationship("PublishingRecord", backref="author", lazy=True, cascade="all, delete-orphan")

    def __init__(self, first_name, last_name, email, password,qualifications):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        # self.qualifications = qualifications


    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def getPublications(self):
        pass

    def getPublicationTree(self):
        pass

    def toDict(self):
        return{
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            # 'qualifications': [qualification for qualification in self.qualifications]
        }

