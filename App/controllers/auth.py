from flask_jwt import JWT

def authenticate(email, password):
    author = Author.query.filter_by(email=email).first()
    if author and author.check_password(password):
        return author
    return None

# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return Author.query.get(payload['identity'])

def setup_jwt(app):
    return JWT(app, authenticate, identity)