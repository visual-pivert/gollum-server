from apiflask import APIFlask
from domain.account.routes import account_app
from bootstrap import Bootstrap
from domain.access.routes import access_app
from domain.user.routes import user_app
from domain.contrib.routes import contrib_app
from domain.repo.routes import repo_app
import os
import subprocess
import threading

app = APIFlask(__name__)

bootstrap = Bootstrap()

def gitolite_setup_async():
    bin_path = os.getenv("BIN_PATH")
    git_conf_path = os.getenv("GIT_COMPILED_CONF_PATH")
    repo_dir = os.getenv("REPO_DIR")

    try:
        # setup gitolite (bloquant ici mais dans un thread séparé)
        subprocess.run([f"{bin_path}/gitolite", "setup"], check=True)

        # corriger les droits après compilation
        subprocess.run(["sudo", "chown", "-R", "www-data:www-data", git_conf_path])
        subprocess.run(["sudo", "chmod", "777", "-R", git_conf_path])
        subprocess.run(["sudo", "chmod", "777", "-R", repo_dir])

    except subprocess.CalledProcessError as e:
        app.logger.error(f"Erreur gitolite setup: {e}")

@app.before_request
def before_request_gitolite_setup():
    # lancer le setup en thread détaché, non bloquant
    threading.Thread(target=gitolite_setup_async, daemon=True).start()

@app.route("/")
def home():
    return "Hello Flask!", 200

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
app.register_blueprint(repo_app)
