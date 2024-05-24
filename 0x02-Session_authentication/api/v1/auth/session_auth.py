#!/usr/bin/env python3
"""
session_auth
"""
from api.v1.auth.auth import Auth
import uuid


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
        if session_id is None or not isinstance(session_id, str):
            return None
        self.user_id_by_session_id[session_id] = session_id
        return self.user_id
        