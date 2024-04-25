from flask import Flask
from domain.account.routes import account_app
from bootstrap import Boostrap
from domain.auth.routes import auth_app

app = Flask(__name__)

bootstrap = Boostrap()


@app.route('/')
def index():
    return "je suis la page d'accueil"


# Register all apps routes
app.register_blueprint(account_app)
app.register_blueprint(auth_app)

