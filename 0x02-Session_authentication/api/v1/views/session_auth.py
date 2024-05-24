#!/usr/bin/env python3
""" Module of Session Authentication views """
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User
from os import getenv

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /auth_session/login
    Logs in a user with email and password, returns session ID as cookie
    """
    from api.v1.app import auth

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({"email": email})
    except Exception:
        users = []

    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    cookie_name = getenv("SESSION_NAME")

    response = jsonify(user.to_json())
    response.set_cookie(cookie_name, session_id)

    return response
