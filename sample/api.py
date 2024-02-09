from flask import jsonify
from sqlalchemy import select

from sample.cache import cache
from sample.db import db_session
from sample.models import User

NUM_OF_CANDIDATE_POSTS = 100
NUM_OF_POSTS_TO_RETURN = 10


def healthcheck():
    try:
        db_session.execute(select(1))
        return jsonify({"status": "healthy"}), 200
    except Exception as e:
        print(f"db health check failed: {e}")
        return jsonify({"status": "unhealthy"}), 500


@cache.memoize(timeout=10)
def get_user(user_id):
    try:
        user = db_session.get(User, user_id)

        return make_response(user)
    except Exception as e:
        print(f"api failed: {e}")
        return jsonify({}), 500


def post_user(name, email):
    user = User(name, email)
    db_session.add(user)
    db_session.commit()
    response = make_response(user)
    response.headers["Location"] = "/api/users/%d" % user.id
    return response, 201


def make_response(user):
    return jsonify({"id": user.id, "name": user.name})
