from flask import Flask
from domain.account.routes import account_app
from bootstrap import Boostrap

app = Flask(__name__)

bootstrap = Boostrap()


@app.route('/')
def index():
    return "je suis la page d'accueil"


# Register all apps routes
app.register_blueprint(account_app)
