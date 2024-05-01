from apiflask import APIFlask
from domain.account.routes import account_app
from bootstrap import Bootstrap
from domain.repo.routes import repo_app
from domain.access.routes import access_app

app = APIFlask(__name__)

bootstrap = Bootstrap()

# Register all apps routes
app.register_blueprint(account_app)
app.register_blueprint(repo_app)
app.register_blueprint(access_app)

