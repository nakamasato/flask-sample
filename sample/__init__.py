from flask import Flask, request

from sample import api
from sample.cache import init_cache
from sample.db import db_session, init_db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    init_db()
    init_cache(app)

    @app.route("/health")
    def healthcheck():
        return api.healthcheck()

    @app.route("/users/<int:user_id>", methods=["GET"])
    def get_user(user_id=None):
        return api.get_user(user_id)

    @app.route("/users", methods=["POST"])
    def post_user():
        payload = request.json
        return api.post_user(payload.get("name"), payload.get("email"))

    return app


app = create_app()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run()
