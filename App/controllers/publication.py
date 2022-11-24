from App.models import Publication
from App.database import db

def create_publication(title, authors, coauthors):
    #Need to do a check on the coauthors before creating the publication to make default accounts for nonexistent ones.
    new_publication = Publication(title, authors, coauthors)
    db.session.add(new_publication)
    db.session.commit()
    return new_publication

def get_publication(id):
    return Publication.query.get(id)

def get_all_publications():
    return Publication.query.all()

def get_all_publications_json():
    publications = Publication.query.all()
    if not publications:
        return []
    publications = [publication.toJSON() for publication in publications]
    return publications