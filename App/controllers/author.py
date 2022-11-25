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

def get_author_by_name(first_name,last_name):
    print(first_name,last_name)
    authors = Author.query.filter_by(first_name=first_name)
    authors.query.filter_by(last_name = last_name).all()
    return authors
    # if not authors:                               This section needs to be reviewed, can't create author without 
    #     new_author = create_author(name=name)     relevant parameters
    #     authors = [new_author]
    #     return authors
    
def create_default_author_account(first_name,last_name):
    password = last_name+first_name
    email = first_name+"."+last_name+"@mail.com"
    new_author = create_author(first_name, last_name, password,email)
    if new_author != None:
        db.session.add(new_author)
        db.session.commit()
        return True
    else:
        return False

def get_author_by_id(id):
    author = Author.query.filter_by(id=id).all()
    return author

def create_new_author_account():
    pass

def get_author_publications(id):
    author = get_author(id)
    if not author:
        return []
    return author.get_publications()


# def publication_tree(authorId):
#     traversed_auths = []
#     root_pubs = []
#     root_co_auths= []
#     root_pubs = get_author_publications(authorId)
#     traversed_auths.append(authorId)
#     for pub in root_pubs:
#         current_auths= pub.getAuthors()
#         for auth in current_auths:
#             if traversed_auths.contains(auth.id) == False:
#                 traversed_auths.append(auth.id)
#                 root_pubs.extend(get_author_publications(auth.id))

#     pub_tree = []
#     for auth in traversed_auth:
#         pub_tree.extend(publication_tree(auth))

#     return pub_tree
        


# def getpublicationtree(id):
#     author = get_author(id)
#     if not author:
#         return []
#     return author.get_publications()
    