from flask_login import login_user, logout_user, LoginManager


login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def authenticate(email, password):
    author = Author.query.filter_by(email=email).first()
    if author and author.check_password(password):
        return author
    return None

def loginuser(user, remember):
    return login_user(user, remember=remember)

def logoutuser():
    logout_user()

# Payload is a dictionary which is passed to the function by Flask JWT
# def identity(payload):
#     return Author.query.get(payload['identity'])

# def setup_jwt(app):
#     return JWT(app, authenticate, identity)