from flask import Flask
from domain.account.routes import account_app

app = Flask(__name__)


@app.route('/')
def index():
    return "je suis la page d'accueil"


# Register all apps routes
app.register_blueprint(account_app)
