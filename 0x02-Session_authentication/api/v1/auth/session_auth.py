#!/usr/bin/env python3
"""
session_auth
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User
from api.v1.views import app_views
from flask import jsonify, request, abort


class SessionAuth(Auth):
    """
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ Destroy a session based on the session ID """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        if session_id not in self.user_id_by_session_id:
            return False
        del self.user_id_by_session_id[session_id]
        return True
