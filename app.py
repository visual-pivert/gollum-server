from flask import Flask
from domain.account.routes import account_app
from bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "42d31e41fb18761c0a147e59b51ccb2169bb1a27096c110c41557932b17ee275"


bootstrap = Bootstrap()


@app.route('/')
def index():
    return "je suis la page d'accueil"


# Register all apps routes
app.register_blueprint(account_app)
