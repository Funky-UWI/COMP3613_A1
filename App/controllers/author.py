from App.models import Author
from App.database import db

def create_author(first_name,last_name,email,password, qualifications): #qualifications
    new_author = Author(first_name=first_name,last_name=last_name,email=email,password=password,qualifications= qualifications)
    db.session.add(new_author)
    db.session.commit()
    return new_author

def get_author(id):
    return Author.query.get(id)

def get_all_authors():
    return Author.query.all()

def get_all_authors_json():
    authors = Author.query.all()
    if not Author:
        return []
    authors = [author.toJSON() for author in authors]
    return authors

def get_author_by_name(name):
    print(name)
    authors = Author.query.filter_by(name=name)
    authors = [author for author in authors]
    # this code should be in a different method

    if not authors:
        new_author = create_author(name=name, dob=None, qualifications=None)
        authors = [new_author]
        return authors
    return authors

def create_new_author_account():
    pass

def get_author_publications(id):
    author = get_author(id)
    if not author:
        return []
    return author.get_publications()

def getpublicationtree(id):
    author = get_author(id)
    if not author:
        return []
    return author.get_publications()
    