"""Application entry point.

A small reporting service built with Flask. The application is assembled
by a factory that registers the request-handling blueprints and returns a
ready-to-run app instance.
"""

from flask import Flask

from views.reports import reports
from views.files import files
from views.proxy import proxy


def create_app():
    """Build and configure the reporting application.

    Registers the request-handling blueprints and returns the app so it can
    be run directly or served by a WSGI host.
    """
    app = Flask(__name__)

    app.register_blueprint(reports)
    app.register_blueprint(files)
    app.register_blueprint(proxy)

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app


if __name__ == "__main__":
    create_app().run()
