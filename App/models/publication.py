from App.database import db

class Publication(db.Model):
    __tablename__ = "publication"
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(120), nullable=False, unique=True)
    # fields = db.Column("fields", db.ARRAY(db.String(60)), nullable=False)
    publication_date = db.Column("publication_date", db.DateTime, nullable=False)
    records = db.relationship("PublishingRecord", backref="publication", lazy=True, cascade="all, delete-orphan")

    def __init__(self, title, fields, publication_date):
        self.title = title
        # self.fields = fields
        self.publication_date = publication_date

    def getAuthors(self):
        pass
    
    def toDict(self):
        return{
            "id": self.id,
            "title": self.title,
            # "fields": [field for field in self.fields],
            "publication_date": self.publication_date
        }

