from flask import Flask, request
from sample.db import db_session, init_db
from sample.cache import init_cache
from sample import api


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    init_db()
    init_cache(app)

    @app.route('/health')
    def healthcheck():
        return api.healthcheck()

    @app.route('/users')
    def get_user():
        user_id = request.args.get('user_id', default=1, type=int)
        return api.get_user(user_id)

    return app


app = create_app()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
