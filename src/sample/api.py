from flask import jsonify
from sample.models import User
from sample.db import db_session
from sample.cache import cache

NUM_OF_CANDIDATE_POSTS = 100
NUM_OF_POSTS_TO_RETURN = 10


def healthcheck():
    try:
        db_session.execute('SELECT 1')
        return jsonify({
            'status': 'healthy'
        }), 200
    except Exception as e:
        print(f'db health check failed: {e}')
        return jsonify({
                'status': 'unhealthy'
            }), 500


@cache.memoize(timeout=10)
def get_user(user_id):
    try:
        user = User.query.get(user_id)

        return make_response(user)
    except Exception as e:
        print(f'api failed: {e}')
        return jsonify({}), 500


def make_response(user):
    return jsonify({
        "id": user.id,
        "name": user.name
    })
