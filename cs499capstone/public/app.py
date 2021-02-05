# pip
from flask import Flask, g


def create_app():
    app = Flask(__name__)
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    with app.app_context():
        from cs499capstone.public import routes

        app.register_blueprint(routes.bp)

    @app.teardown_appcontext
    def teardown(error):
        psql = g.pop("psql", None)
        if psql:
            psql.close()

    return app
