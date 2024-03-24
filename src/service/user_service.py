from os import environ
from flask import jsonify, make_response

TEST = environ.get("TEST")


def get_users_all():
    response = make_response(
        jsonify([{"name": "John Doe", "email": "john@test.com"}]), 200
    )
    return response


def get_user(id):
    response = make_response(
        jsonify(
            {
                "name": "John Doe",
                "email": "john@test.com",
            }
        ),
        200,
    )
    return response


def post_user(data):
    response = make_response(jsonify(data), 200)
    return response
