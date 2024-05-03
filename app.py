from apiflask import APIFlask
from domain.account.routes import account_app
from bootstrap import Bootstrap
from domain.access.routes import access_app
from domain.user.routes import user_app
from domain.contrib.routes import contrib_app

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
app.register_blueprint(access_app)
app.register_blueprint(user_app)
app.register_blueprint(contrib_app)
