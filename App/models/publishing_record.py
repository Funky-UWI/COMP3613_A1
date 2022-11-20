from App.database import db

class PublishingRecord(db.Model):
    __tablename__ = "publishing_record"
    id = db.Column("id", db.Integer, primary_key=True)
    author_id = db.Column("author_id", db.Integer, db.ForeignKey("author.id"))
    publication_id = db.Column("publication_id", db.Integer, db.ForeignKey("publication.id"))

    def toDict(self):
        return {
            "id": self.id,
            "author_id": self.author_id,
            "publication_id": self.publication_id
        }