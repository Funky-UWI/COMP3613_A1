from App.models import Author
from App.database import db

def create_author(first_name, last_name, email, password):
    new_author = Author(first_name=first_name, last_name=last_name, email=email, password=password)
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
    authors = Author.query.filter_by(first_name=name).all()
    authors = list(authors)
    # this code should be in a different method

    authors.append(list(Author.query.filter_by(last_name=name).all()))

    # if not authors:                               This section needs to be reviewed, can't create author without 
    #     new_author = create_author(name=name)     relevant parameters
    #     authors = [new_author]
    #     return authors
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
    