from apiflask import APIFlask
from domain.account.routes import account_app
from bootstrap import Bootstrap
from domain.repo.routes import repo_app
from domain.access.routes import access_app

app = APIFlask(__name__)

bootstrap = Bootstrap()


@app.error_processor
def error_handler(error):
    return {
        'status_code': error.status_code,
        'message': error.message,
        'detail': error.detail
    }, error.status_code, error.headers


# Register all apps routes
app.register_blueprint(account_app)
app.register_blueprint(repo_app)
app.register_blueprint(access_app)
